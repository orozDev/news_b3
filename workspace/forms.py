from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
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


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        exclude = (
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'user_permissions',
            'groups',
            'last_login',
            'password'
        )


# password = forms.CharField(validators=[validate_password])
