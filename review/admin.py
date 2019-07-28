from django.contrib import admin
from .models import Review, Image
from .forms import ReviewPostForm, ImagePostForm


class ImageAdmin(admin.ModelAdmin):
    list_display = ('review', 'image')


admin.site.register(Review)
admin.site.register(Image, ImageAdmin)
