from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Image, Like, Comment
from .serializers import ImageSerializer, ReviewSerializer, CommentSerializer, ReviewListSerializer
from users.models import User



class SearchReviewList(APIView):
    def get(self, request, format=None):
        review = Review.objects.all()
        serializer = ReviewListSerializer(review, many=True)
        return Response(serializer.data)


class ReviewView(APIView):
    def get(self, request, format=None):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = request.data
        if 'activity' in data:
            activity = data.pop('activity')
        else:
            activity = []
        if 'subject' in data:
            subject = data.pop('subject')
        else:
            subject = []
        if 'region' in data:
            region = data.pop('region')
        else:
            region = []
        serializer = ReviewSerializer(data=request.data)

        # images = ImageSerializer()
        try:
            if serializer.is_valid():
                serializer.save(user=user, activity=activity,
                                subject=subject, region=region)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    def get(self, request, review_id, format=None):
        reivew = get_object_or_404(Review, id=review_id)
        serializer = ReviewSerializer(reivew)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MyReviewView(APIView):
    def get(self, request, pk, format=None):
        reviews = User.objects.get(id=pk).reviews
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


class LikeReview(APIView):
    def post(self, request, review_id, format=None):
        user = request.user
        review = get_object_or_404(Review, id=review_id)
        try:
            Like.objects.get(creator=user, review=review)
            return Response(status=status.HTTP_304_NOT_MODIFIED)
        except Like.DoesNotExist:
            Like.objects.create(creator=user, review=review)
            return Response(status=status.HTTP_201_CREATED)


class CommentView(APIView):
    def get(self, reqeust, review_id, format=None):
        review = get_object_or_404(Review, id=review_id)
        comments = review.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, review_id, format=None):
        user = request.user
        review = get_object_or_404(Review, id=review_id)

        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(created_by=user, review=review)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
