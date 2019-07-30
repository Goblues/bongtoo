from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=255)
    region = models.ManyToManyField(
        "commons.Region", related_name="region_users",blank=True)
    activity = models.ManyToManyField(
        "commons.Activity", related_name="activity_users", blank=True)
    subject = models.ManyToManyField(
        "commons.Subject", related_name="subject_users",blank=True)
    profile_image = models.ImageField(
        upload_to='images/', null=True, max_length=None, blank=True)
