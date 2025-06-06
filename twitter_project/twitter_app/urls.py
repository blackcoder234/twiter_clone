from django.urls import path
from . import views

urlpatterns = [
    path("", views.app, name="app"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("back/", views.back, name="back"),
    path("add_tweet/", views.add_tweet, name="add_tweet"),
    path("user_profile/<int:user_id>/", views.user_profile, name="user_profile"),
    path("edit_tweet/<int:tweet_id>/", views.edit_tweet, name="edit_tweet"),
    path("delete_tweet/<int:tweet_id>/", views.delete_tweet, name="delete_tweet"),
    path("edit_user_profile/<int:profile_id>/", views.edit_user_profile, name="edit_user_profile"),
    path("delete_user_profile/<int:profile_id>/", views.delete_user_profile, name="delete_user_profile"),
    path("tweet/<int:tweet_id>/", views.tweet_detail, name="tweet_detail"),
]