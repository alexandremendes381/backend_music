from django.contrib import admin
from django.urls import path, include
from login.views import Cadastroviewsets
from rest_framework import routers
from music.views import Arquivosviewsets, export_audio
from django.conf import settings
from django.conf.urls.static import static
from video.views import VideoViewSet
from postspage.views import postsModelviewsets
from rareimages.views import ImagesModelviewsets
from drf_yasg import openapi

# SWAGGER
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions


router = routers.DefaultRouter()
router.register(r'arquivos', Arquivosviewsets)
router.register(r'cadastro', Cadastroviewsets, basename='cadastro')
router.register(r'videos', VideoViewSet)
router.register(r'posts', postsModelviewsets)
router.register(r'ImagesRare', ImagesModelviewsets)


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('rest_framework.urls')),
    path('export/audio/<int:audio_id>/', export_audio, name='export_audio'),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
