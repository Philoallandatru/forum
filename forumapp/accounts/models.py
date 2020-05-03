from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    signature = models.CharField(max_length=255, blank=True, null=True)
    head_img = models.ImageField(height_field=150, width_field=150, blank=True, null=True)
    friends = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return "" + self.username
