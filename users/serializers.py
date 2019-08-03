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
        print('validated', validated_data)
        activity_data = validated_data.pop('activity', [])
        subject_data = validated_data.pop('subject', [])
        region_data = validated_data.pop('region', [])

        for data in region_data:
            region = Region.objects.get(
                city=data['city'], town=data['town']
            )
            instance.region.set(region)

        print('activity_data', activity_data)
        datas = []
        for data in activity_data:
            activity = Activity.objects.get(
                id=data['id'])
            datas.append(activity)
        
        instance.activity.set(datas)

        for data in subject_data:
            subject = Subject.objects.get(
                id=data['id'])
            instance.subject.set(subject)

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
