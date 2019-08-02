from .views import ApiRoot
from review.restviews import SearchReviewList, ReviewView, MyReviewView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib import admin
admin.autodiscover()

# rest_framework

# app's view

admin.site.login = login_required(admin.site.login)

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # root
    path('', ApiRoot.as_view(), name="api"),
    # auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # user
    path('users/', include('users.urls')),
    # review
    path('api/search/reviews/', SearchReviewList.as_view(), name="search_reviews"),
    path('api/reviews/', ReviewView.as_view(), name="reviews"),
    # path('api/<pk>/reviews/', MyReviewView.as_view(), name="my_review"),
    # path('api/search/service/')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
