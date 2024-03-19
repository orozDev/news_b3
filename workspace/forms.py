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


class ChangeProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия'}),
        }


class ChangePasswordForm(forms.Form):

    def __init__(self, user=None, *args, **kwargs):
        self.user: User = user
        super().__init__(*args, **kwargs)

    password = forms.CharField(label='Текущий пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(label='Новый пароль', validators=[validate_password],
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='Подтвердите пароль',
                                       widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')

        if not self.user.check_password(password):
            raise forms.ValidationError({'password': ['The password is incorrect']})

        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if confirm_password != new_password:
            raise forms.ValidationError({'confirm_password': ['The passwords do not match']})

        return cleaned_data