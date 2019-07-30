from django.contrib import admin
from .models import Target, Activity


class TargetInline(admin.TabularInline):
    model = Target


class ActivityInline(admin.TabularInline):
    model = Activity


# Register your models here.
admin.site.register(Target)
admin.site.register(Activity)
