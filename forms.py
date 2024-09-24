from django import forms
from django.forms import ModelForm
from .models import *
class LoginForm(forms.ModelForm):
    class Meta:
        model=Login
        fields=['Username','Password']
class SignupForm(forms.ModelForm):
    class Meta:
        model=Signup
        fields='__all__'
