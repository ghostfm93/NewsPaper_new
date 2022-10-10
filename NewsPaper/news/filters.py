import django_filters
from .models import Post
from django.forms import DateTimeInput, DateInput


class PostFilter(django_filters.FilterSet):

    dateCreation = django_filters.DateFilter(
        field_name='created',
        lookup_expr='gt',
        label='Date',
        widget=DateInput(
            format='%Y-%m-%d',
            attrs={'type': 'date'},
        ),
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'post_author',
            'category',
        ]

