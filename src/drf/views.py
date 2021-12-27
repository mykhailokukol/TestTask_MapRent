from django.shortcuts import render
from . import serializers
from app import models
from rest_framework import viewsets


class AdViewSet(viewsets.ModelViewSet):
    queryset = models.Advertisement.objects.all()
    serializer_class = serializers.AdSerializer
