from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from . import forms
from .models import User, Friend
from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.contrib import messages



# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

# class UserDetail(DetailView):
#     model = User


def UserProfilePage(request, username):
    # user = User.objects.filter(username=username)
    post_user = User.objects.prefetch_related("posts").get(username__iexact=username)
    posts = post_user.posts.all()
    comments = post_user.comments.all()
    my_friends = request.user.friends.all()
    # his_friends = Friend.objects.get(current_user = post_user).users.all()
    context = {
        'posts' : posts,
        'comments' : comments,
        'this_user' : post_user,
        'my_friends' : my_friends,
        # 'his_friends' : his_friends,

    }
    return render(request, "accounts/user_profile.html", context)



# def add_friend(request, pk):

#     return 


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect(friend.get_absolute_url())

def follows_him(request, pk):
    him = User.objects.get(pk=pk)
    request.user.friends.add(him)

    return redirect(him)


def unfollows_him(request, pk):
    him = User.objects.get(pk=pk)
    request.user.friends.remove(him)

    return redirect(him)

def UserFans(request, username):
    # user = User.objects.filter(username=username)
    post_user = User.objects.prefetch_related("posts").get(username__iexact=username)
    posts = post_user.posts.all()
    comments = post_user.comments.all()
    my_friends = request.user.friends.all()
    # his_friends = Friend.objects.get(current_user = post_user).users.all()
    context = {
        'posts' : posts,
        'comments' : comments,
        'this_user' : post_user,
        'my_friends' : my_friends,
        # 'his_friends' : his_friends,

    }
    return render(request, "accounts/user_fans.html", context)

def UserFollows(request, username):
    # user = User.objects.filter(username=username)
    post_user = User.objects.prefetch_related("posts").get(username__iexact=username)
    posts = post_user.posts.all()
    comments = post_user.comments.all()
    my_friends = request.user.friends.all()
    # his_friends = Friend.objects.get(current_user = post_user).users.all()
    context = {
        'posts' : posts,
        'comments' : comments,
        'this_user' : post_user,
        'my_friends' : my_friends,
        # 'his_friends' : his_friends,

    }
    return render(request, "accounts/user_following.html", context)


def updateProfile(request, username):
    if request.method == 'POST':
        _form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if _form.is_valid():
            _form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect(request.user)
    else:
        _form = UserUpdateForm(instance=request.user)


    context = {
        'form' : _form,
        'username' : request.user.username
    }

    return render(request, "accounts/user_profile_edit.html" , context=context)


def editUserProfile(request, username):
    if request.method == 'POST':
        _form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if _form.is_valid():
            _form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect(request.user)
    else:
        _form = UserUpdateForm(instance=request.user)


    context = {
        'form' : _form,
        'username' : request.user.username
    }

    return render(request, "accounts/user_profile_update.html" , context=context)