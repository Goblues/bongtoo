from django.db import models

# Create your models here.


class Target(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name


class Activity(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name
