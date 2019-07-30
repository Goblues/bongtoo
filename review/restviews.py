from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review, Image
from .serializers import ImageSerializer, LikeSerializer, ReviewSerializer, CommentSerializer

reviews = Review.objects.all()

class SearchReviewList(APIView):
    def get(self, request, format=None):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
