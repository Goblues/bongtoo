from django.contrib import admin
from .models import Region, Activity, Subject


class ActivityInline(admin.TabularInline):
    model = Activity

class RegionInline(admin.TabularInline):
    model = Region

class SubjectInline(admin.TabularInline):
    model = Subject


# Register your models here.
admin.site.register(Region)
admin.site.register(Activity)
admin.site.register(Subject)
