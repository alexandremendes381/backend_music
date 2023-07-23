from rest_framework import viewsets
from .models import termsModel
from .serializers import termsModelSerializer


class termsModelviewsets(viewsets.ModelViewSet):
    queryset = termsModel.objects.all()
    serializer_class = termsModelSerializer
    http_method_names = ["post", "get", "patch"]
