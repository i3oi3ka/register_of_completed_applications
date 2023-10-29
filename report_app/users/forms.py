from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your nick'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your surname'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Your birthday'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat your password'}))
    avatar = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Avatar'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'birthday', 'email', 'password1', 'password2', 'avatar']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class ChangeUserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['birthday', 'first_name', 'last_name', 'email', 'avatar']
        widgets = {
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата народження'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Прізвище'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Імя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'avatar'}),

        }


