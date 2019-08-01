from django.contrib import admin
from .models import Review, Image, Comment, Like


class ImageInline(admin.TabularInline):
    model = Image


class CommentInline(admin.TabularInline):
    model = Comment


class LikeInline(admin.TabularInline):
    model = Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'creator', 'created_at')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'review', 'image')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
    inlines = [
        ImageInline, CommentInline, LikeInline
    ]


admin.site.register(Review, ReviewAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
admin.site.register(Like, LikeAdmin)
