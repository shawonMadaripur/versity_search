from django.db import models

# Create your models here.

class AllList(models.Model):
  Country = models.CharField(max_length=30)
  Institute = models.CharField(max_length=100)
  Professors = models.CharField(max_length=50)
  Research_Area = models.CharField(max_length=30)
  URL = models.CharField(max_length=100)