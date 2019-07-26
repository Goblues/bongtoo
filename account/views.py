from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import AccountUserCreationForm, AccountUserChangeForm, AccountAuthenticationForm, AccountUserInformationForm
from .models import Region, Activity, User


from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


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
                reverse('select')
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
    return render(request, "home.html")


@csrf_exempt
def select(request):
    if request.method == 'POST':
        accountUserInformationForm = AccountUserInformationForm(request.POST)
        if accountUserInformationForm.is_valid:
            user = accountUserInformationForm.save
            user.region = accountUserInformationForm.cleaned_data['region']
            user.activity = accountUserInformationForm.cleaned_data['activity']
            user.save()
            return HttpResponseRedirect(
                reverse('home')
            )
        else:
            return HttpResponseRedirect('home')
    elif request.method == 'GET':
        accountUserInformationForm = AccountUserInformationForm()
    return render(request, "select.html", {"accountUserInformationForm": accountUserInformationForm, })


'''
def select(request):
    regionlist = Region.objects.all()
    activitylist = Activity.objects.all()
    return render(request, "select.html", {'regionlist': regionlist, 'activitylist': activitylist, })


def selectinformation(request):
    user = request.user
    if request.method == 'POST':
        regionfield = request.POST.get('regionchoice')
        activityfield = request.POST.get('activitychoice')
        user.region = regionfield
        user.activity = activityfield
        user.save()
    return redirect('home')
'''
