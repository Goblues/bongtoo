from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.models import User
from account.serializers import UserSerializer

from review.models import Review, Like
from review.serializers import ReviewListSerializer


class UserLV(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDV(APIView):
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserLikeView(APIView):
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        likes = user.likes.all()
        serializer = ReviewListSerializer(likes, many=True)
        return Response(serializer.data)
