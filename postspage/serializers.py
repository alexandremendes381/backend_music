from .models import postsModel
from rest_framework import serializers


class postsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = postsModel
        fields = '__all__'
