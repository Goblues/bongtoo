from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255)
    target = models.ManyToManyField(
        "commons.Target", related_name="users", blank=True)
    activity = models.ManyToManyField(
        "commons.Activity", related_name="users", blank=True)
    grandcity = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    profile_image = models.ImageField(
        upload_to='images/', null=True, max_length=None, blank=True)
