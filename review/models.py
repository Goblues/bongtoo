from django.db import models
from django.conf import settings


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="reviews",
                             null=True, on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=True, max_length=100)
    body = models.TextField(null=True)
    region = models.ManyToManyField(
        "commons.Region", related_name="region_reivews", blank=True)
    activity = models.ManyToManyField(
        "commons.Activity", related_name="activity_reivews", blank=True)
    subject = models.ManyToManyField(
        "commons.Subject", related_name="subject_reivews", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']

    @property
    def get_thumnail(self):
        return self.images.first()        # return self.images.get(id=1).image

    @property
    def like_count(self):
        return self.likes.all().count()

    def __str__(self):
        return self.title
  


class Comment(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review, related_name="comments", null=True, on_delete=models.CASCADE)
    body = models.CharField(null=True, max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "username : {}, body : {}, create_at : {}".format(self.created_by.username, self.body, self.created_at)


class Image(models.Model):
    review = models.ForeignKey(
        Review, related_name="images", blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', max_length=None, null=True, blank=True)


class Like(models.Model):
    review = models.ForeignKey(
        Review, related_name="likes", null=True, on_delete=models.CASCADE)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="likes",  null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "user : {}, create_at : {}".format(self.creator.username, self.created_at)
