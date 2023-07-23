from .models import termsModel
from rest_framework import serializers


class termsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = termsModel
        fields = '__all__'
