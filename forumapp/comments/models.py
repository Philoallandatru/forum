from posts.models import Post
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from accounts.models import User


# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments"

    )
    parent_comment = models.ForeignKey(
        'self', blank=True, null=True, related_name='my_children', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=1024, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.content) == 0:
            raise ValidationError('评论内容不能为空')

    def __str__(self):
        return "<" + self.content + "> to (" + self.post.message + ") by [" + self.user.username + "]"

    def get_absolute_url(self):
        return reverse("comments:comment_detail", kwargs={"pk": self.pk})

