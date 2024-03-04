from django import forms

from news.models import Category, Tag


class NewsForm(forms.Form):
    name = forms.CharField(label='Заголовок',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}))

    image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Краткое описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    category = forms.ModelChoiceField(label='Категория', queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    tags = forms.ModelMultipleChoiceField(label='Теги', queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())
