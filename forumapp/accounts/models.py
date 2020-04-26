from django.db import models
from django.contrib import auth
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    signature = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField(null=True, blank=True)
    




# # Create your models here.
# class User(auth.models.User, auth.models.PermissionsMixin):
#     # signature = models.CharField(max_length=255, blank=True, null=True)

#     def __str__(self):
#         return "@{}".format(self.username)


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    # signature = models.CharField(max_length=255, blank=True, null=True)
    # online = models.BooleanField(default=False)

#     def __str__(self):
#         return self.name


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)