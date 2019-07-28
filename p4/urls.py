from django.contrib import admin
from django.urls import path
import account.views
import review.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account.views.home, name='home'),
    path('signup/', account.views.signup, name='signup'),
    path('signin/', account.views.signin, name='signin'),
    path('signout/', account.views.signout, name='signout'),
    # path('select/', account.views.select, name='select'),
    # path('<username>/', review.views.mypage),
    # path('<username>/<int:review_id>/', review.views.reviewdetail),
    path('post/', review.views.post, name='post'),
]
