from .models import ArquivosModel
from rest_framework import serializers


class ArquivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArquivosModel
        fields = '__all__'
