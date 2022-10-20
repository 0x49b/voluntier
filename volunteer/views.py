from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import VolunteerType
from .serializers import VolunteerTypeSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def volunteertype_list(request):
    if request.method == 'GET':
        data = VolunteerType.objects.all()
        serializer = VolunteerTypeSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VolunteerTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def volunteertype_detail(request, pk):
    try:
        volunteer_type = VolunteerType.objects.get(pk=pk)
    except VolunteerType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # todo implement all for this method
    if request.method == 'PUT':
        serializer = VolunteerTypeSerializer(volunteer_type, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        volunteer_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
