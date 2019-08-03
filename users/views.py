from django.conf import settings
# rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

# rest_auth
from rest_auth.registration.views import RegisterView
from rest_auth.utils import jwt_encode
from rest_auth.app_settings import (TokenSerializer,
                                    JWTSerializer,
                                    create_token)
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings

# my app
from commons.models import Region, Activity, Subject
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer

from review.models import Review, Like
from review.serializers import LikedReviewSerializer, ReviewListSerializer


class UserLV(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserCreateView(RegisterView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permissions_class = (permissions.AllowAny)

    def perform_create(self, serializer):
        validated_data = self.request.data
        user = serializer.save(
            self.request)
        if getattr(settings, 'REST_USE_JWT', False):
            self.token = jwt_encode(user)
        else:
            create_token(self.token_model, user, serializer)

        complete_signup(self.request._request, user,
                        allauth_settings.EMAIL_VERIFICATION,
                        None)

        subject_data = validated_data.pop('subject')
        activity_data = validated_data.pop('activity')
        regions_data = validated_data.pop('region')

        for data in regions_data:
            region = Region.objects.get(
                city=data['city'], town=data['town']
            )
            user.region.add(region)

        for data in activity_data:
            activity = Activity.objects.get(
                id=data['id'])
            user.activity.add(activity)

        for data in subject_data:
            subject = Subject.objects.get(
                id=data['id'])
            user.subject.add(subject)
        return user


class UserDV(APIView):
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserLikeView(APIView):
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        likes = user.likes.all()
        serializer = LikedReviewSerializer(likes, many=True)
        return Response(serializer.data)


class UserReviewView(APIView):
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        reviews = user.reviews.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
