from django.contrib import admin
from network.models import *

class PostDisplay(admin.ModelAdmin):
    list_display = ['author', 'text', 'created_at', 'updated_at',]
    filter_horizontal = ['liked_by',]

# Register your models here.
admin.site.register(User)
admin.site.register(Post, PostDisplay)
