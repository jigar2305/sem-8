from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username', 'password','email','role','phone_number')


class updateForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=10)
    class Meta():
        model = User
        fields = ('username','email','phone_number','picture','address','city','state','country','pincode')
