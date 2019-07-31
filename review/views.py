from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from .models import Review, Image
from .forms import ReviewPostForm, ImagePostForm, CommentPostForm


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


def post_comment(request):
    if request.method == "POST":
        commentPostForm = CommentPostForm(request.POST)
        if CommentPostForm.is_valid():
            commentpost = CommentPostForm.save(commit=False)
            commentpost.user = request.user
            commentpost.save()
            return redirect('home')
    else:
        commentPostForm = CommentPostForm()
        return render(request, "detail.html", {'commentPostForm': CommentPostForm, })


def detail(request, review_id):
    reviewid = get_object_or_404(Review, id=review_id)
    context = {
        'reviewid': reviewid,
    }
    return render(request, "detail.html", context)
