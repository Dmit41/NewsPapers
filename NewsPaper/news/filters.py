from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateTimeFilter
from django.forms import DateTimeInput
from .models import News, Category


class NewsFilter(FilterSet):
    name = CharFilter(
        field_name='name',
        lookup_expr='icontains',
        label='Заголовок содержит:'
    )

    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все категории'
    )

    date = DateTimeFilter(
        field_name='date',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
        label='Дата позже:'
    )

    class Meta:
        model = News
        fields = {
            'name', 'category', 'date'
        }
