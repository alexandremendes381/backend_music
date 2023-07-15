from rest_framework import viewsets
from .models import postsModel
from .serializers import postsModelSerializer


class postsModelviewsets(viewsets.ModelViewSet):
    queryset = postsModel.objects.all()
    serializer_class = postsModelSerializer
    http_method_names = ["post", "get", "patch"]
