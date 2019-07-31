from rest_framework import serializers
# app
from review.models import Review, Comment, Image, Like
# commons
from commons.serializers import RegionSerializer, SubjectSerializer, ActivitySerializer
# account
from account.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'title',
            'body',
            'get_thumnail',
        )


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    region = RegionSerializer(many=True)
    subject = SubjectSerializer(many=True)
    activity = ActivitySerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'title',
            'body',
            'created_at',
            'updated_at',
            'user',
            'region',
            'subject',
            'activity',
            'comments',
            'like_count'
        ]
