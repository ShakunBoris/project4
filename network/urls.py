
from django.urls import path

from . import views

urlpatterns = [
    # pages
    path("", views.index, name="index"),
    path('user/<str:profile>', views.profile, name='profile'),
    path('following', views.following, name='following'),
    # commands
    path("post", views.post, name="post"),
    # API
    # path('user/<str:profile>', views.profile, name='profile')
    # USE SAME AS PROFILE BUT 'PUT FOR FETCH
    
    # service
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
