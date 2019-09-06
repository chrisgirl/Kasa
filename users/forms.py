from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=250, required=True, widget=forms.TextInput(attrs={
        "class": "form-control my-input",
        "id": "form-username",
        "placeholder": "Username..."
    }))
    email = forms.EmailField(max_length=200, required=True, widget=forms.TextInput(attrs={
        "class": "form-control my-input",
        "id": "form-email",
        "placeholder": "Email..."
    }))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class": 'form-control my-input',
        "name": "password",
        "id": "password",
        "placeholder": "Password..."
    }))

    password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        "class": 'form-control my-input',
        "name": "password",
        "id": "password2",
        "placeholder": "Confirm Password..."
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
