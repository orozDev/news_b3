from django import forms

from news.models import Category, News


# class NewsForm(forms.Form):
#     name = forms.CharField(label='Заголовок',
#                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}))
#
#     image = forms.ImageField(label='Изображение', widget=forms.FileInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(label='Краткое описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
#     category = forms.ModelChoiceField(label='Категория', empty_label='sds', queryset=Category.objects.all(),
#                                       widget=forms.Select(attrs={'class': 'form-select'}))
#     tags = forms.ModelMultipleChoiceField(label='Теги', queryset=Tag.objects.all(),
#                                           widget=forms.CheckboxSelectMultiple())
#

class NewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'] = forms.ModelChoiceField(label='Категория', empty_label='Choose an item',
                                                          queryset=Category.objects.all(),
                                                          widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = News
        fields = (
            'name',
            'image',
            'description',
            'content',
            'category',
            'tags'
        )

        # labels = {
        #     'name': 'Заголовок 1'
        # }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(),
        }
