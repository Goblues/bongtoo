from django.urls import path
from .restviews import LikeReview, ReviewView, ReviewDetailView

app_name = 'review'

urlpatterns = [
    path('', ReviewView.as_view(), name="list"),
    path('<review_id>/', ReviewDetailView.as_view(), name="detail"),
    path('<review_id>/like', LikeReview.as_view(), name="like")
]
