from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import Review, Image
from .forms import ReviewPostForm, ImagePostForm


def post(request):
    if request.method == "POST":
        reviewPostForm = ReviewPostForm(request.POST)
        imagePostForm = ImagePostForm(request.POST, request.FILES)
        if reviewPostForm.is_valid() and imagePostForm.is_valid:
            reviewpost = reviewPostForm.save(commit=False)
            reviewpost.user = request.user
            reviewpost.save()
            imagepost = imagePostForm.save(commit=False)
            imagepost.review = reviewpost
            imagepost.image = imagePostForm.clean_image()
            imagepost.save()
            return redirect('home')
    else:
        reviewPostForm = ReviewPostForm()
        imagePostForm = ImagePostForm()
        return render(request, "post.html", {'reviewPostForm': ReviewPostForm, 'imagePostForm': ImagePostForm, })
