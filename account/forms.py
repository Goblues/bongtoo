from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User, Region, Activity
from django.core.files.images import get_image_dimensions


class AccountAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'palceholder': 'Username',
                'required': 'True',
            }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'required': 'True',
            }))


class AccountUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'True',
            }
        )
    )
    username = forms.RegexField(label='Username',
                                max_length=30,
                                regex=r'^[\w.@+-]+$',
                                help_text="Required.",
                                error_messages={'invalid': "This"},
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Username',
                                           'required': 'True', }))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Password',
                                           'required': 'True', }))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Password confirmation',
                                           'required': 'True', }),
                                help_text="Enter")
    name = forms.RegexField(label='Nickname',
                            max_length=30,
                            regex=r'^[\w.@+-]+$',
                            help_text="Required.",
                            error_messages={'invalid': "This"},
                            widget=forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': 'Nickname',
                                       'required': 'True', }))
    #name = forms.CharField(label='Nickname', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nickname', 'required': 'True', }))
    grandcity = forms.CharField(label='Grandcity', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Grandcity', 'required': 'True', }))
    city = forms.CharField(label='City', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'City', 'required': 'True', }))
    #profile_image = forms.ImageField(label='Profile_Image', widget=forms.PictureWidget)
    region = forms.ModelChoiceField(
        label='Region', queryset=Region.objects.all())
    activity = forms.ModelChoiceField(
        label='Activity', queryset=Activity.objects.all())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'name', 'grandcity', 'city', 'profile_image', 'region', 'activity', )

    def clean_image(self):
        profile_image = self.cleaned_data['profile_image']
        return profile_image


class AccountUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')


# class AccountUserInformationForm(forms.ModelForm):
#     region = forms.ModelChoiceField(queryset=Region.objects.all())
#     activity = forms.ModelChoiceField(queryset=Activity.objects.all())

#     class Meta:
#         model = User
#         fields = ('region', 'activity')
