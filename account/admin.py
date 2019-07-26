from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User, Region, Activity
from .forms import AccountUserCreationForm, AccountUserChangeForm, AccountAuthenticationForm, AccountUserInformationForm

User = get_user_model()


class AccountUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + \
        (('User', {'fields': ('name', 'grandcity', 'city',
                              'region', 'activity', 'profile_image',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        (('User', {'fields': ('name', 'grandcity', 'city',
                              'region', 'activity', 'profile_image',), }),)
    add_form = AccountUserCreationForm


admin.site.register(User, AccountUserAdmin)
admin.site.register(Region)
admin.site.register(Activity)
