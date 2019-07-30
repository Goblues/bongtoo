from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import AccountUserCreationForm, AccountUserChangeForm, AccountAuthenticationForm

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

