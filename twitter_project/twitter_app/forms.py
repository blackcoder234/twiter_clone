from django import forms
from .models import Tweet, UserProfile, User
import re
import random

class customSignupForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm_Password")
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")
        
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")

       
        if name:
            parts = name.strip().split()
            if len(parts) == 1:
                base = parts[0][:10]
            else:
                base = (parts[0] + parts[1][0]).lower()[:10]
            username_base = re.sub(r'[^a-z0-9_]', '', base.lower())
        elif email:
            username_base = re.sub(r'[^a-z0-9_]', '', email.split("@")[0].lower())[:10]
        else:
            username_base = "user"

        if len(username_base) < 3:
            username_base += ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=3))

        
        for _ in range(10):  
            number = str(random.randint(10, 9999))
            username = f"{username_base[:15-len(number)]}{number}"
            if not User.objects.filter(username=username).exists():
                break
        else:
            
            username = f"{username_base[:11]}{random.randint(10000,99999)}"

        cleaned_data["username"] = username
        return cleaned_data


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'What\'s happening?'}),
            'photo': forms.ClearableFileInput(attrs={'multiple': False}),
        }
    
    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) > 280:
            raise forms.ValidationError("Tweet cannot exceed 280 characters.")
        return text


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
            'avatar': forms.ClearableFileInput(),
        }
    
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) > 200:
            raise forms.ValidationError("Bio cannot exceed 200 characters.")
        return bio