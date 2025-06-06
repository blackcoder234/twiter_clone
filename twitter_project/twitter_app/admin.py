from django.contrib import admin
from .models import UserProfile, Tweet
from django.utils.html import format_html

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user', 'user_full_name', 'user_email', 'bio', 'avatar_thumb')
    search_fields = ('user__username', 'user__email', 'bio')
    # list_filter = ('user__is_active', 'user__date_joined')
    list_select_related = ('user',)
    readonly_fields = ('user',)
    ordering = ('user__username',)

    def user_id(self, obj):
        return obj.user.id
    user_id.short_description = 'User ID'

    def user_full_name(self, obj):
        return obj.user.get_full_name()
    user_full_name.short_description = 'Full Name'

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = 'Email'
    
    def avatar_thumb(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="48" height="48" style="object-fit:cover; border-radius:6px;" />', obj.avatar.url)
        return "-"
    avatar_thumb.short_description = 'avatar'



@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_text', 'photo_thumb', 'created_at', 'updated_at')
    search_fields = ('user__username', 'text')
    # list_filter = ('created_at', 'user')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    def short_text(self, obj):
        return (obj.text[:50] + '...') if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Text'
    
    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="48" height="48" style="object-fit:cover; border-radius:6px;" />', obj.photo.url)
        return "-"
    photo_thumb.short_description = 'Photo'