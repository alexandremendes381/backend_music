from .models import ImagesModel
from rest_framework import serializers


class ImagesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = '__all__'
