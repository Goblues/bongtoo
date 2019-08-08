from .views import ApiRoot
from review.restviews import SearchReviewList, ReviewView, MyReviewView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from django.contrib import admin
# admin.autodiscover()

# rest_framework
from allauth.account.views import confirm_email
# app's view
from services.views import ServiceListView

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # root
    path('', ApiRoot.as_view(), name="api"),
    # auth
    path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
            confirm_email, name='account_confirm_email'),
    # user
    path('users/', include('users.urls')),
    # review
    path('search/reviews/', SearchReviewList.as_view(), name="search_reviews"),
    path('search/volunteer/', ServiceListView.as_view(), name="search_volunteers"),
    path('reviews/', include('review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
