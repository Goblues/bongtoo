from .views import ApiRoot
from review.restviews import SearchReviewList, ReviewView, MyReviewView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf.urls import url
# admin.autodiscover()

# rest_framework
from allauth.account.views import confirm_email
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view
from django.urls import include
# app_name = "docs"

schema_view = get_schema_view(
   openapi.Info(
      title="Bongtoo API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="petepp@naver.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(AllowAny,),
)
urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # root
    path('', ApiRoot.as_view(), name="api"),
    path('rest-auth/', include('rest_auth.urls')),
    # auth
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    re_path(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
    # user
    path('users/', include('users.urls')),
    # review
    path('api/search/reviews/', SearchReviewList.as_view(), name="search_reviews"),
    path('reviews/',include('review.urls')),
    # path('v1/', include('docs.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
