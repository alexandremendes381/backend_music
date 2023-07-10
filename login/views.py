from rest_framework import viewsets
from .models import CadastroModel
from .serializers import CadastroSerializer
from django_filters import rest_framework as filters
from .filters import CadastroFilter
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response


class Cadastroviewsets(viewsets.ModelViewSet):
    queryset = CadastroModel.objects.all()
    serializer_class = CadastroSerializer
    http_method_names = ["post", "get", "patch"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CadastroFilter

    @action(detail=False, methods=["patch"])
    def update_password(self, request, pk=None):
        email = request.data.get('email')
        new_password = request.data.get('password')

        cadastros = CadastroModel.objects.filter(email=email)
        for cadastro in cadastros:
            cadastro.password = new_password
            cadastro.save()

        if cadastros:
            return Response({"message": "Senha atualizada com sucesso!"})
        else:
            return Response({"message": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
