from django.contrib import admin
<<<<<<< HEAD
from .models import Target, Activity


class TargetInline(admin.TabularInline):
    model = Target
=======
from .models import Region, Activity, Subject
>>>>>>> feature/data_init


class ActivityInline(admin.TabularInline):
    model = Activity


# Register your models here.
<<<<<<< HEAD
admin.site.register(Target)
admin.site.register(Activity)
=======
admin.site.register(Region)
admin.site.register(Activity)
admin.site.register(Subject)
>>>>>>> feature/data_init
