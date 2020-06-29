from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class User(AbstractUser):
    signature = models.CharField(max_length=255, blank=True, null=True)
    head_img = models.ImageField(blank=True, null=True, upload_to='profile_pics', default="default.jpeg")
    friends = models.ManyToManyField("User", blank=True, related_name='followed_by')

    def __str__(self):
        return "" + self.username

    def get_absolute_url(self):
        return reverse(
            "accounts:profile",
            kwargs={
                "username": self.username,
            }
        )

    
    # def get_connections(self):
  	# 	connections = Connection.objects.filter(creator=self.user)
  	# 	return connections
          
    # def get_followers(self):
    #     followers = Connection.objects.filter(following=self.user)
    #     return followers


class Friend(models.Model):
    users = models.ManyToManyField(User, blank=True)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

