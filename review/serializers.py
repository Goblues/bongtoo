from rest_framework import serializers
# app
from review.models import Review, Comment, Image, Like
# commons
from commons.models import Region, Activity, Subject
from commons.serializers import RegionSerializer, SubjectSerializer, ActivitySerializer
# account
from users.serializers import UserSerializer, UserRoughList

ActivityModel = Activity
class CommentSerializer(serializers.ModelSerializer):
    created_by = UserRoughList()
    class Meta:
        model = Comment
        fields = [
            'id',
            'body',
            'created_by',
            'created_at',
        ]


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = Image
        fields = [
            'id',
            'image'
        ]


class ReviewListSerializer(serializers.ModelSerializer):
    get_thumnail = ImageSerializer(read_only=True)

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
    user = UserSerializer(required=False)
    region = RegionSerializer(
        many=True, source="region_reivews", required=False)
    subject = SubjectSerializer(
        many=True, source='subject_reivews', required=False)
    activity = ActivitySerializer(
        many=True, required=False)
    comments = CommentSerializer(many=True, required=False)
    images = ImageSerializer(many=True, required=False)

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
            'like_count',
            'images'
        ]

    def create(self, validated_data):
        try:
            subject_data = validated_data.pop('subject')
            activity_data = validated_data.pop('activity')
            regions_data = validated_data.pop('region')
            review = Review.objects.create(**validated_data)
            
            for data in regions_data:
                region, created = Region.objects.get(
                    city=data['city'], town=data['town']
                )
                review.region.add(region)

            for data in activity_data:
                activity = Activity.objects.get(
                    id=data['id'])
                review.activity.add(activity)

            for data in subject_data:
                subject, created = Subject.objects.get(
                    id=data['id'])
                review.subject.add(subject)
        except:
            review.delete()
        finally:
            return review
