from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Volunteer
from .serializers import VolunteerSerializer
# Create your views here.


class ServiceListView(APIView):
    def get(self, request, format=None):
        filters = {
            'activityclass__in': request.GET.getlist('activites'),
            'subjectclass__in': request.GET.getlist('subjects'),
            'city': request.GET.get('city'),
            'region': request.GET.get('town')
        }
        filters = dict(filter(lambda item: item[1], filters.items()))
        volunteer = Volunteer.objects.filter(
            **filters)
        serializer = VolunteerSerializer(volunteer, many=True)
        return Response(serializer.data)
