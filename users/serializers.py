from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from django.conf import settings
# app
from users.models import User
from review.models import Review
from commons.models import Activity, Subject, Region
# commons
from commons.serializers import RegionSerializer, ActivitySerializer, SubjectSerializer


class UserSerializer(serializers.ModelSerializer):
    region = RegionSerializer(many=True)
    activity = ActivitySerializer(many=True)
    subject = SubjectSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'profile_image',
            'region',
            'activity',
            'subject'
        ]


class UserCreateSerializer(RegisterSerializer):
    email = serializers.EmailField(required=False)
    region = RegionSerializer(
        many=True, required=False)
    subject = SubjectSerializer(
        many=True, required=False)
    activity = ActivitySerializer(
        many=True, required=False)