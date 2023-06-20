from rest_framework import viewsets
from .models import ArquivosModel
from .serializers import ArquivoSerializer
from django.http import FileResponse, HttpResponse
from .filters import ArquivosFilter
from django_filters import rest_framework as filters

# Create your views here.


class Arquivosviewsets(viewsets.ModelViewSet):
    queryset = ArquivosModel.objects.all()
    serializer_class = ArquivoSerializer
    http_method_names = ["post", "get", "patch", "delete"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArquivosFilter

def export_audio(request, audio_id):
    try:
        audio = ArquivosModel.objects.get(id=audio_id)
        response = FileResponse(audio.audio_file.open(), as_attachment=True)
        return response
    except ArquivosModel.DoesNotExist:
        return HttpResponse("Áudio não encontrado", status=404)
