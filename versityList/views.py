from django.shortcuts import render
from .serializers import AllListSerializer
from .models import AllList
from rest_framework import viewsets

# Create your views here.

class AllListViewSet(viewsets.ModelViewSet):
  queryset = AllList.objects.all()
  serializer_class = AllListSerializer

  def get_queryset(self):
    queryset = super().get_queryset()

    country = self.request.query_params.get('country', None)
    reasearch = self.request.query_params.get('reasearch', None)

    if reasearch is not None and country is not None:
      queryset = queryset.filter(Research_Area__contains = reasearch, Country = country)
    elif country is not None:
      queryset = queryset.filter(Country = country)
    elif reasearch is not None:
      queryset = queryset.filter(Research_Area = reasearch)
    
    return queryset