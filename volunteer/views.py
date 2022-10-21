from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

from .models import VolunteerType
from .serializers import VolunteerTypeSerializer


class VolunteerTypeViewSet(viewsets.ModelViewSet):
    queryset = VolunteerType.objects.all()
    serializer_class = VolunteerTypeSerializer
    permission_classes = [permissions.IsAuthenticated]