
from django.urls import path

from . import views

urlpatterns = [
    # pages
    path("", views.index, name="index"),
    path('user/<str:profile>', views.profile, name='profile'),
    # commands
    path("post", views.post, name="post"),
    # API
    
    # service
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
