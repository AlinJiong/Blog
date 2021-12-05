from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django import forms
from captcha.fields import CaptchaField


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)


class UserRegiterForm(forms.ModelForm):
    password = forms.CharField(max_length=20)
    password2 = forms.CharField(max_length=20)

    captcha = CaptchaField(label='验证码',
                           required=True,
                           error_messages={'required': '验证码不能为空'})

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("两次输入密码不一致，请重试")