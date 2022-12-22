from django.contrib import admin
from network.models import *


class FollowersInline(admin.TabularInline):
    model = User.followed_by.through
    fk_name ='to_user'
class AdminDisplay(admin.ModelAdmin):
    filter_horizontal = ['followed_by',]
    inlines = [FollowersInline,]    
class PostDisplay(admin.ModelAdmin):
    list_display = ['author', 'text', 'created_at', 'updated_at',]
    filter_horizontal = ['liked_by',]

# Register your models here.
admin.site.register(User, AdminDisplay)
admin.site.register(Post, PostDisplay)
