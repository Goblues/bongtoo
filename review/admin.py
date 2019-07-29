from django.contrib import admin
from .models import Review, Image
from .forms import ReviewPostForm, ImagePostForm


class ImageAdmin(admin.ModelAdmin):
    list_display = ('review', 'image')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
