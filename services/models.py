from django.db import models

# Create your models here.
class Volunteer(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255)
    term = models.CharField(null=True, blank=True, max_length=100)
    starttime = models.DateTimeField(null=True, blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    field = models.CharField(null=True, blank=True, max_length=255)
    place = models.CharField(null=True, blank=True, max_length=255)
    subject = models.CharField(null=True, blank=True, max_length=255)
    value = models.CharField(null=True, blank=True,
                             unique=True, max_length=100)
    subjectclass = models.CharField(null=True, blank=True, max_length=100)
    activityclass = models.CharField(null=True, blank=True, max_length=100)
    city = models.CharField(null=True, blank=True, max_length=100)
    town = models.CharField(null=True, blank=True, max_length=100)

    class Meta:
        ordering = ('endtime',)

    def __str__(self):
        return self.title
