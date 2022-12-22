
from django.urls import path

from . import views

urlpatterns = [
    # pages
    # path("", views.index, name="index"),
    # path("post_list", views.PostsPages.as_view(), name='post_list'),
    path("", views.PostsPages.as_view(), name='index'),
    path('user/<str:profile>', views.ProfilePages.as_view(), name='profile'),
    path('following', views.Following.as_view(), name='following'),
    # path('following', views.following, name='following'),
    # commands
    path("post", views.post, name="post"),
    # API
    # path('user/<str:profile>', views.profile, name='profile')
    # USE SAME AS PROFILE BUT 'PUT FOR FETCH
    path('edit/<int:postpk>', views.edit, name='edit'),
    
    # service
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
