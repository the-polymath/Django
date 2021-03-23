from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class registerform(UserCreationForm):
    email = forms.EmailField()
    number = forms.IntegerField()

    class Meta:
        model = User
        fields = ["username", "email", "number", "password1", "password2"]
