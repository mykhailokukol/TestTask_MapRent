from rest_framework import serializers
from app import models


class AdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Advertisement
        fields = '__all__'