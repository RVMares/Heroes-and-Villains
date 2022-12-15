from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':

        queryset = Supers.objects.all()
        custom_response_dictionary = {}

        heroes= queryset.filter(super_type__super_type = "hero")
        villains= queryset.filter(super_type__super_type = "villain")
        serialized_heroes = SupersSerializer(heroes, many=True)
        serialized_villains = SupersSerializer(villains, many=True)
        if request.query_params.get("super_type") == "hero":
            custom_response_dictionary = serialized_heroes.data
        elif request.query_params.get("super_type") == "villain":
            custom_response_dictionary = serialized_villains.data
        else:
            custom_response_dictionary = {
                "heroes": serialized_heroes.data,
                "villains": serialized_villains.data
                }

        return Response(custom_response_dictionary, status= status.HTTP_200_OK)
    
    
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers);
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

