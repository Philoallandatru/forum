from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
import misaka

from groups.models import Group
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=200, blank=True )
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    likes = models.ManyToManyField(User, blank=True, related_name="post_likes")

    # notes for related name: therefore you can use group.posts to reference all the posts in the group
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
    
    def get_like_url(self):
        return reverse("posts:likes_toggle", kwargs={"pk" : self.id})

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]
