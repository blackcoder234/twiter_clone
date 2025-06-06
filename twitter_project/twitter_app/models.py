from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    
    def __str__(self):
        return self.user.username

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    text = models.TextField(max_length=280)
    photo = models.ImageField(upload_to="tweet_photos/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.text}"