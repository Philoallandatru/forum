from posts.models import Post
from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import MyUser

# Create your models here.


class Comment(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self',blank=True,null=True,related_name='my_children', on_delete=models.CASCADE)
    MyUser = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="CommentUser")
    content = models.TextField(max_length=1024, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if len(self.content) == 0:
            raise ValidationError(_('评论内容不能为空'))

    def __str__(self):
        return "<" + self.content + "> to (" + self.post.message + ") by [" + self.MyUser.MyUsername + "]"

