from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.pagination import PageNumberPagination

from .models import Volunteer
from .serializers import VolunteerSerializer
# Create your views here.


class ServiceListView(APIView, PageNumberPagination):
    page_size = 8

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
        result = self.paginate_queryset(volunteer, request, view=self)
        serializer = VolunteerSerializer(result, many=True)

        return self.get_paginated_response(serializer.data)
