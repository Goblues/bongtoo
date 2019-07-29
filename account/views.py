from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import AccountUserCreationForm, AccountUserChangeForm, AccountAuthenticationForm
from .models import Region, Activity, User
from review.models import Review, Image
from django.views.decorators.csrf import csrf_exempt


def signup(request):
    if request.method == 'POST':
        accountUserCreationForm = AccountUserCreationForm(
            request.POST, request.FILES)
        if accountUserCreationForm.is_valid():
            user = accountUserCreationForm.save(commit=False)
            user.email = accountUserCreationForm.cleaned_data['email']
            user.profile_image = accountUserCreationForm.clean_image()
            user.save()
            login(request, user)
            return HttpResponseRedirect(
                reverse('home')
            )
    elif request.method == 'GET':
        accountUserCreationForm = AccountUserCreationForm()
    return render(request, "signup.html", {"accountUserCreationForm": accountUserCreationForm, })


def signin(request):
    if request.method == 'POST':
        accountAuthenticationForm = AccountAuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(
                reverse('home')
            )
        else:
            return HttpResponseRedirect('login failed')
    else:
        accountAuthenticationForm = AccountAuthenticationForm()
        return render(request, "signin.html", {"accountAuthenticationForm": accountAuthenticationForm, })


def signout(request):
    logout(request)
    return redirect('home')


def home(request):
    reviews = Review.objects.all()
    images = Image.objects.all()
    return render(request, "home.html", {'reviews': reviews, 'images': images, })


# @csrf_exempt
# def select(request):
#     if request.method == 'POST':
#         accountUserInformationForm = AccountUserInformationForm(request.POST)
#         if accountUserInformationForm.is_valid:
#             session = accountUserInformationForm.save(commit=False)
#             session.user = request.user
#             return HttpResponseRedirect(
#                 reverse('home')
#             )
#         else:
#             return HttpResponseRedirect('home')
#     elif request.method == 'GET':
#         accountUserInformationForm = AccountUserInformationForm()
#     return render(request, "select.html", {"accountUserInformationForm": accountUserInformationForm, })
