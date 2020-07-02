from django.urls import path
from . import views

app_name='comments'

urlpatterns = [
    path('by/<username>/<int:pk>/', views.CommentDetail, name="user_comment_detail"),
    path('delete/<int:pk>', views.CommentDetail),
    path('detail/<int:pk>', views.CommentDetail.as_view(), name="comment_detail"),
    path("new/", views.CreateComment.as_view(), name="create_comment"),
    path("for/<username>/<int:pk>/", views.CommentPostCreate.as_view(), name="postComment"),
    path("detail/<int:pk>/<username>/<int:parent>/", views.CommentToComment.as_view(), name="commentToComment"),
]
