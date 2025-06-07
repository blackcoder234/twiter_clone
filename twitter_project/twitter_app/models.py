from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(max_length=200, blank=True)
    avatar = CloudinaryField("avatar", folder="user_avatars", blank=True, null=True)

    def __str__(self):
        return self.user.username

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    text = models.TextField(max_length=280)
    photo = CloudinaryField("photo", folder="tweet_photos", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.text}"