from rest_framework import viewsets
from .models import ImagesModel
from .serializers import ImagesModelSerializer


class ImagesModelviewsets(viewsets.ModelViewSet):
    queryset = ImagesModel.objects.all()
    serializer_class = ImagesModelSerializer
    http_method_names = ["post", "get", "patch"]
