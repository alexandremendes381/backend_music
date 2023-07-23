from django_filters import rest_framework as filters
from .models import CadastroModel


class CadastroFilter(filters.FilterSet):
    email = filters.CharFilter(field_name="email", lookup_expr="exact")

    resultado = filters.CharFilter(method='filter_resultado')

    class Meta:
        model = CadastroModel
        fields = (
            "email",
            "password"
        )

    def filter_resultado(self, queryset, name, value):
        if value.strip() == '':
            raise filters.ValidationError(
                'O resultado não pode ser em branco.')
        return queryset.filter(**{name: value})
