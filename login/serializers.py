from .models import CadastroModel
from rest_framework import serializers


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroModel
        fields = '__all__'
