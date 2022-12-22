import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from network.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import *
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class PostsPages(ListView):
    model = Post 
    paginate_by = 10
    template_name = 'network/index.html'
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['form'] = PostForm()
            context['posts'] = Post.objects.all().order_by('-created_at')
            return context
    def get_ordering(self):
        return ['-created_at']

@method_decorator(csrf_exempt, name='dispatch')
class ProfilePages(ListView):
    model = Post 
    paginate_by = 10
    template_name = 'network/profile.html'
    def get_queryset(self):
        # print('!!!!!!!!!!!!!!!!!!!', self.kwargs['profile'])
        user = User.objects.get(username=self.kwargs['profile'])
        result = Post.objects.filter(author=user)
        return result
    def get_ordering(self):
        return ['-created_at']
    def get_context_data(self, **kwargs):
        user = User.objects.get(username=self.kwargs['profile'])
        context = super().get_context_data(**kwargs)
        context['user_viewed'] =  user.username 
        context['followed_by'] = user.followed_by.values_list('username', flat=True)
        context['is_following'] = user.is_following.all()
        return context      
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        if data.get('folUnfol') is not None:
            if request.user not in User.objects.get(username=self.kwargs['profile']).followed_by.all():
                User.objects.get(
                    username=self.kwargs['profile']).followed_by.add(request.user)
            else:
                User.objects.get(
                    username=self.kwargs['profile']).followed_by.remove(request.user)
        return HttpResponse(status=204)
        
        
# @csrf_exempt
# def profile(request, profile):
#     if request.method == 'GET':
#         user = User.objects.get(username=profile)
#         user_info = {
#             'user_viewed': profile,
#             'followed_by': user.followed_by.values_list('username', flat=True),
#             'is_following': user.is_following.all(),
#             'posts':  Post.objects.filter(author=user).order_by('-created_at')
#         }
#         return render(request, 'network/profile.html', {
#             'user_info': user_info
#         })
#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         if data.get('folUnfol') is not None:
#             if request.user not in User.objects.get(username=profile).followed_by.all():
#                 User.objects.get(
#                     username=profile).followed_by.add(request.user)
#             else:
#                 User.objects.get(
#                     username=profile).followed_by.remove(request.user)
#         return HttpResponse(status=204)

@method_decorator(login_required, name='dispatch')
class Following(ListView):
    model = Post 
    paginate_by = 10
    template_name = 'network/following.html'
    def get_queryset(self):
        follows = self.request.user.is_following.all()
        return Post.objects.filter(author__in=follows)
    def get_ordering(self):
        return ['-created_at']
# def following(request):
#     follows = request.user.is_following.all()
#     posts = Post.objects.filter(author__in=follows).order_by('-created_at')
#     return render(request, 'network/following.html', {
#         'posts': posts,
#     })

@login_required
def post(request):
    ''' METHOD DOESN'T WORK IDC
    form = PostForm(request.POST, initial={'author': request.user})
    form.save()
    '''
    # THIS ONE IS FIRST ON DOCUMENTATION
    new_post = Post(author=request.user)
    form = PostForm(request.POST, instance=new_post)
    if form.is_valid():
        form.save()
    ''' method 3 WORKS !!!!! But more code
    # form = PostForm(request.POST)
    # new_post = form.save(commit=False)
    # new_post.author = request.user
    # new_post.save()
    '''
    return HttpResponseRedirect(reverse("index"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
