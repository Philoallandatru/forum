from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
import misaka

from groups.models import Group
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(
        Group, related_name="posts",null=True, 
        blank=True,on_delete=models.CASCADE
    )

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
