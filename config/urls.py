from django.contrib import admin
from django.urls import path
import account.views
import review.views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


from review.restviews import SearchReviewList, ReviewView, MyReviewView
from account.views import UserLV, UserDV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', UserLV.as_view()),
    path('api/users/<user_id>/', UserDV.as_view()),
    path('api/search/reviews/', SearchReviewList.as_view(), name="search_review"),
    path('api/reviews/', ReviewView.as_view()),
    path('api/<pk>/reviews/', MyReviewView.as_view(), name="my_review")
    # path('api/search/service/')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = format_suffix_patterns(urlpatterns)
