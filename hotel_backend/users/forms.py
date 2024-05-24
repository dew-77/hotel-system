from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = [
            'email', 'first_name', 'last_name',
            'patronymic', 'phone_number', 'password'
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError(
                'Пароль должен содержать как минимум 8 символов')
        return password
