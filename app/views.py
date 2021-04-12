from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Travel
from rest_framework import generics
from .serializers import TravelSerializer
from rest_framework.decorators import api_view, renderer_classes
# Create your views here.

@api_view(['GET'])
def CapiOverview(request, format=None):
    return Response({
        'Travel List': reverse('class-travel-list', request=request, format=format),
    })

@api_view(['GET',])
def FapiOverview(request, format=None):
    api_urls = {
        'List':'/func-travel-data/',
        'Detail View':'/func-travel-detail/<int:pk>/',
        'Create':'/func-travel-create/',
        'Update':'/func-travel-update/<int:pk>/',
        'Delete':'/func-travel-delete/<int:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def travelList(request):
    inst = Travel.objects.all()
    serializer = TravelSerializer(inst, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def travelDetail(request, pk):
    inst = Travel.objects.get(id=pk)
    serializer = TravelSerializer(inst, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def travelCreate(request):
    data = request.data
    serializer = TravelSerializer(data=data)

    if serializer.is_valid():
        if data["d_from"] == data["d_to"]:
            return Response("You are already there")
        elif not Travel.objects.filter(d_from=data["d_from"], d_to=data["d_to"], date=data["date"]).exists():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response("data is already there")
    

    


@api_view(['POST'])
def travelUpdate(request, pk):
    inst = Travel.objects.get(id=pk)
    serializer = TravelSerializer(instance=inst, data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def travelDelete(request, pk):
    inst = Travel.objects.get(id=pk)
    inst.delete()

    return Response("Item successfully deleted!")




class TravelList(generics.ListCreateAPIView):

    queryset = Travel.objects.all()

    serializer_class = TravelSerializer

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer