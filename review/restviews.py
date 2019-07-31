from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Image
from .serializers import ImageSerializer, LikeSerializer, ReviewSerializer, CommentSerializer, ReviewListSerializer


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
