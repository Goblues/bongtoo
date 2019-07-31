from django.contrib import admin
from django.urls import path
import account.views
import review.views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


from review.restviews import SearchReviewList
# resturlpatterns = [
#     path('reviews/', restviews.Review.as_view(), name="search_review")
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.home, name='home'),
    path('signup/', account.views.signup, name='signup'),
    path('signin/', account.views.signin, name='signin'),
    path('signout/', account.views.signout, name='signout'),
    # path('select/', account.views.select, name='select'),
    path('post/', review.views.post, name='post'),
    path('<username>/', account.views.page, name='page'),
    path('api/search/reviews/', SearchReviewList.as_view(), name="search_review"),
    # path('api/search/service/')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = format_suffix_patterns(urlpatterns)
