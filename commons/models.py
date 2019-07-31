from django.db import models

# Create your models here.


<<<<<<< HEAD
class Target(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
=======
class Region(models.Model):
    city = models.CharField(null=True, blank=True, max_length=100)
    town = models.CharField(null=True, blank=True, max_length=100)
>>>>>>> feature/data_init

    def __str__(self):
        return '{},{}'.format(self.city, self.town)


class Activity(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{},{}'.format(self.id, self.name)


class Subject(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{},{}'.format(self.id, self.name)
