from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# rest_framework
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# jwt
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

# app's view
from review.restviews import SearchReviewList, ReviewView, MyReviewView
from .views import ApiRoot
# app's urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRoot.as_view(), name="api"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', include('account.urls')),
    path('api/search/reviews/', SearchReviewList.as_view(), name="search_reviews"),
    path('api/reviews/', ReviewView.as_view(), name="reviews"),
    # path('api/<pk>/reviews/', MyReviewView.as_view(), name="my_review"),
    # path('api/search/service/')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = format_suffix_patterns(urlpatterns)
