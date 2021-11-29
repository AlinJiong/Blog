from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    pwd = forms.CharField(max_length=20)