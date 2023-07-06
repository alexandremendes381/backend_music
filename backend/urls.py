from django.contrib import admin
from django.urls import path, include
from login.views import Cadastroviewsets
from rest_framework import routers
from music.views import Arquivosviewsets, export_audio
from django.conf import settings
from django.conf.urls.static import static
from video.views import VideoViewSet
router = routers.DefaultRouter()
router.register(r'arquivos', Arquivosviewsets)
router.register(r'cadastro', Cadastroviewsets)
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('rest_framework.urls')),
    path('export/audio/<int:audio_id>/', export_audio, name='export_audio'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
