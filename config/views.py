from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


class ApiRoot(APIView):
    def get(self, request, format=None):
        return Response({
            'users': reverse('users', request=request, format=format),
            'reviews': reverse('review:list', request=request, format=format),
            'seacrch_reviews': reverse('search_reviews', request=request, format=format),
        })
