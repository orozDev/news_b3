import django_filters
from django import forms

from news.models import News, Tag


class NewsFilter(django_filters.FilterSet):

    tags_name = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), field_name='tags',
                                                         widget=forms.CheckboxSelectMultiple())
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = News
        fields = (
            'date',
            'category',
        )