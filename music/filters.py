from django_filters import rest_framework as filters
from .models import ArquivosModel


class ArquivosFilter(filters.FilterSet):
    artist = filters.CharFilter(field_name="artist", lookup_expr="icontains")

    class Meta:
        model = ArquivosModel
        fields = (
            "artist",
        )
