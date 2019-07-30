from django.db import models

# Create your models here.


class Region(models.Model):
    city = models.CharField(null=True, blank=True, max_length=100)
    town = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{},{}'.format(self.city, self.town)


class Activity(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.name
