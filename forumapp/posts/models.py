from django.db import models
from django.conf import settings
from django.urls import reverse
from accounts.models import MyUser
# pip install misaka‰
import misaka

from groups.models import Group

from django.contrib.auth import get_user_model


class Post(models.Model):
    MyUser = models.ForeignKey(MyUser, related_name="PostUser",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "MyUsername": self.MyUser.MyUsername,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["MyUser", "message"]
