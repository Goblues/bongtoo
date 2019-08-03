from django.urls import path
from .views import UserLV, UserDV, UserLikeView, UserReviewView, UserCreateView

urlpatterns = [
    path('', UserLV.as_view(), name="users"),
    path('registration/', UserCreateView.as_view(), name="user_create"),
    path('<user_id>/', UserDV.as_view(), name="user_detail"),
    path('<user_id>/likes', UserLikeView.as_view(), name="user_likes"),
    path('<user_id>/reviews', UserReviewView.as_view(), name="user_review")
]
