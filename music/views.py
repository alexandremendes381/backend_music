import os
from django.conf import settings
from rest_framework import viewsets
from .models import ArquivosModel
from .serializers import ArquivoSerializer
from django.http import JsonResponse, FileResponse, HttpResponse
from .filters import ArquivosFilter
from django_filters import rest_framework as filters



class Arquivosviewsets(viewsets.ModelViewSet):
    queryset = ArquivosModel.objects.all()
    serializer_class = ArquivoSerializer
    http_method_names = ["post", "get", "patch", "delete"]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ArquivosFilter


def list(self, request, *args, **kwargs):
    cantores = ArquivosModel.objects.values_list(
        'artist', flat=True).distinct()
    results = []

    for cantor in cantores:
        pasta = {
            'cantor': cantor,
            'link': f'media/musicas/{cantor}',
            'arquivos': []
        }
        pasta_path = os.path.join(settings.MEDIA_ROOT, 'musicas', cantor)

        if os.path.isdir(pasta_path):
            arquivos = os.listdir(pasta_path)
            for arquivo in arquivos:
                arquivo_link = f'{pasta_path}/{arquivo}'
                arquivo_titulo = arquivo[:-4]
                arquivo_imagem = f'{pasta_path}/{arquivo[:-4]}.jpg'
                arquivo_id = self.get_file_id(
                    arquivo_titulo)  # Assign the value here
                arquivo_data = {
                    'id': arquivo_id,
                    'arquivo_link': arquivo_link,
                    'arquivo_imagem': arquivo_imagem,
                    'title': arquivo_titulo,
                }
                pasta['arquivos'].append(arquivo_data)

        results.append(pasta)

    response_data = {'results': results}
    return JsonResponse(response_data)


def export_audio(request, audio_id):
    try:
        audio = ArquivosModel.objects.get(id=audio_id)
        response = FileResponse(audio.music_play.open(), as_attachment=True)
        return response
    except ArquivosModel.DoesNotExist:
        return HttpResponse("Áudio não encontrado", status=404)
