from rest_framework import serializers
# app
from review.models import Review, Comment, Image, Like
# commons
from commons.serializers import RegionSerializer, SubjectSerializer, ActivitySerializer
# account
from users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'id',
            'image'
        ]


class ReviewListSerializer(serializers.ModelSerializer):
    get_thumnail = ImageSerializer(ImageSerializer)

    class Meta:
        model = Review
        fields = (
            'id',
            'title',
            'body',
            'get_thumnail',
        )


class LikedReviewSerializer(serializers.ModelSerializer):
    review = ReviewListSerializer()

    class Meta:
        model = Like
        fields = [
            'id',
            'review',
            'creator',
            'created_at'
        ]


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
