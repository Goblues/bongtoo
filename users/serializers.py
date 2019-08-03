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
    region = RegionSerializer(many=True, required=False)
    activity = ActivitySerializer(many=True, required=False)
    subject = SubjectSerializer(many=True, required=False)

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

    def update(self, instance, validated_data):
        # print('validated', validated_data)
        filed_list = [
            {'instance': Activity, 'field': 'activity'},
            {'instance': Subject, 'field': 'subject'},
            {'instance': Region, 'field':  'region'}
        ]

        for field in filed_list:
            nested_datas = validated_data.pop(field['field'], [])
            datas = []
            for data in nested_datas:
                datas.append(field['instance'].objects.get(**data))
            getattr(instance, field['field']).set(datas)

        return super().update(instance, validated_data)


class UserRoughList(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile_image',
        ]


class UserCreateSerializer(RegisterSerializer):
    email = serializers.EmailField(required=False)
    region = RegionSerializer(
        many=True, required=False)
    subject = SubjectSerializer(
        many=True, required=False)
    activity = ActivitySerializer(
        many=True, required=False)
