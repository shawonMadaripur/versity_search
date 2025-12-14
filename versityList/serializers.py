from rest_framework import serializers
from .models import AllList

class AllListSerializer(serializers.ModelSerializer):
  class Meta:
    model = AllList
    fields = '__all__'