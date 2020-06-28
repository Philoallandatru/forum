from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('profile/<username>/', views.UserProfilePage, name="profile"),
    path('connect/<operation>/<int:pk>/', views.change_friends, name="change_friend"),

    path('follows/<int:pk>', views.follows_him, name="follows_him"),
    path('unfollows/<int:pk>', views.unfollows_him, name="unfollows_him"),

]
