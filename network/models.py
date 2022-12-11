from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followed_by = models.ManyToManyField('self', symmetrical=False, related_name='is_following')
    pass

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(User, related_name='liked_posts')
