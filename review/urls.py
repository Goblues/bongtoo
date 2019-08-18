from django.urls import path
from . import restviews

app_name = 'review'

urlpatterns = [
    path('', restviews.ReviewView.as_view(), name="list"),
    path('<int:review_id>/', restviews.ReviewDetailView.as_view(), name="detail"),
    path('<int:review_id>/images/', restviews.ImageView.as_view(), name="images"),
    path('<int:review_id>/like/', restviews.LikeReview.as_view(), name="like"),
    path('<int:review_id>/comments/',
         restviews.ReviewCommentView.as_view(), name="review_comments"),
    path('comments/', restviews.CommentsView.as_view(), name="comment_list"),
    path('comments/<int:pk>/', restviews.CommetDetailView.as_view(),
         name="comment_detail")
]
