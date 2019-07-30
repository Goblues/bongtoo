from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255)
    region = models.ManyToManyField(
        "commons.Region", related_name="users", null=True)
    activity = models.ManyToManyField(
        "commons.Activity", related_name="users", null=True)
    grandcity = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    profile_image = models.ImageField(
        upload_to='images/', null=True, max_length=None, blank=True)
