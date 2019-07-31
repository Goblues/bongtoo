from rest_framework import serializers
# app
from account.models import User
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
