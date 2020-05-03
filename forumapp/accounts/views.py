from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from . import forms
from .models import User
from django.shortcuts import render
from posts.models import Post


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
    context = {
        'posts' : posts,
        'comments' : comments,

    }
    return render(request, "accounts/user_profile.html", context)




