from django.urls import path
from . import views

app_name='posts'

urlpatterns = [
    path('', views.PostList.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),

    # all the posts posted by a certain user
    path("by/<username>/",views.UserPosts.as_view(),name="for_user"),

    # detail of a single post
    path("by/<username>/<int:pk>/",views.PostDetail.as_view(),name="single"),
    
    path("delete/<int:pk>/",views.DeletePost.as_view(),name="delete"),
    path("post/<int:pk>/likes", views.LikesToggle, name="likes_toggle"),

]
