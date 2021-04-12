from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Travel
from rest_framework import generics
from .serializers import TravelSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def apiOverview(request, format=None):
    return Response({
        'Travel List': reverse('travel-list', request=request, format=format),
    })


class TravelList(generics.ListCreateAPIView):

    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

class TravelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer