from django.contrib import admin
from .models import Review, Image, Comment, Like
from .forms import ReviewPostForm, ImagePostForm
from commons.admin import TargetInline, ActivityInline


class ImageInline(admin.TabularInline):
    model = Image


class CommentInline(admin.TabularInline):
    model = Comment


class LikeInline(admin.TabularInline):
    model = Like


class ImageAdmin(admin.ModelAdmin):
    list_display = ('review', 'image')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    inlines = [
        ImageInline, CommentInline, LikeInline
    ]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
admin.site.register(Like)
