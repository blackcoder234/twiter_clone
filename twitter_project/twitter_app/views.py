from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.models import User
from .models import Tweet, UserProfile, Notification
from django.http import HttpResponse, JsonResponse
from .forms import customSignupForm, TweetForm, UserProfileForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def app(request):
    tweet_list = Tweet.objects.all().order_by('-created_at')
    return render(request, "app/app.html", {'tweet_list': tweet_list})

def signup(request):
    if request.method == 'POST':
        form = customSignupForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            # Create user
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=name
            )

            
            UserProfile.objects.create(user=user)

            messages.success(request, "Account created successfully!")
            return redirect('login')
        else:
            
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
        
    else:
        form = customSignupForm()

    return render(request, 'app/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        user_input = request.POST.get('inputElement')
        password = request.POST.get('password')
        user = None
        if '@' in user_input:
            try:
                user_obj = User.objects.get(email=user_input)
                username = user_obj.username
                user = authenticate(request, username=username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(request, username=user_input, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('app')
        else:
            messages.error(request, "Invalid username/email or password.")
    return render(request, "app/login.html")

def logout(request):
    auth_logout(request)
    return redirect('login')

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)
    has_tweets = user.tweets.exists()
    return render(request, "app/user_profile.html", {
        'user': user,
        'user_profile': user_profile,
        'has_tweets': has_tweets,
    })

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    return render(request, "app/tweet_detail.html", {'tweet': tweet})


def create_tweet_notification(tweet):
    """Create notifications for all followers when a new tweet is posted"""
    # Get all followers of the tweet author
    followers = UserProfile.objects.filter(following=tweet.user.profile)
    
    # Create a notification for each follower
    for follower_profile in followers:
        Notification.objects.create(
            recipient=follower_profile.user,
            sender=tweet.user,
            tweet=tweet,
            notification_type='new_tweet'
        )

@login_required(login_url='login')
def add_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            create_tweet_notification(tweet)
            
            messages.success(request, "Tweet posted successfully!")
            return redirect('app')
    else:
        form = TweetForm()
    return render(request, "app/add_tweet.html", {'form': form})


@login_required
def notifications(request):
    """View to display notifications"""
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    unread_count = notifications.filter(is_read=False).count()
    
    return render(request, "app/notifications.html", {
        'notifications': notifications,
        'unread_count': unread_count
    })

@login_required
def mark_notifications_read(request):
    """Mark notifications as read"""
    if request.method == 'POST':
        notification_ids = request.POST.getlist('notification_ids')
        if not notification_ids:  # If no specific IDs, mark all as read
            Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)
        else:
            Notification.objects.filter(id__in=notification_ids, recipient=request.user).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def notification_count(request):
    """API endpoint to get unread notification count"""
    count = Notification.objects.filter(recipient=request.user, is_read=False).count()
    return JsonResponse({'count': count})

def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('app', tweet_id=tweet.id)
    else:
        form = TweetForm(instance=tweet)
    return render(request, "app/add_tweet.html", {'form': form, 'tweet': tweet})

@login_required
def delete_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    tweet.delete()
    return redirect('app')


def add_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user_profile', user_id=request.user.id)

    else:
        form = UserProfileForm()
    return render(request, "app/add_user_profile.html", {'form': form})

@login_required
def edit_user_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', user_id=request.user.id)

    else:
        form = UserProfileForm(instance=profile)
    return render(request, "app/edit_user_profile.html", {'form': form, 'profile': profile})

def delete_user_profile(request, profile_id):
    profile = get_object_or_404(UserProfile, id=profile_id, user=request.user)
    if request.method == 'POST':
        profile.delete()
        return redirect('app')
    return redirect('app')

def search_tweets(request):
    query = request.GET.get('q', '')
    if query:
        tweet_list = Tweet.objects.filter(content__icontains=query).order_by('-created_at')
    else:
        tweet_list = Tweet.objects.all().order_by('-created_at')
    return render(request, "app/search_tweets.html", {'tweet_list': tweet_list, 'query': query})

def back(request):
    return redirect('app')