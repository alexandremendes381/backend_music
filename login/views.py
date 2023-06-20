from rest_framework import viewsets
from .models import CadastroModel
from .serializers import CadastroSerializer
from django_filters import rest_framework as filters
from .filters import CadastroFilter


class Cadastroviewsets(viewsets.ModelViewSet):
    queryset = CadastroModel.objects.all()
    serializer_class = CadastroSerializer
    http_method_names = ["post", "get"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CadastroFilter
