from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(), label="パスワード")

    class Meta:
        model =User
        fields = ('username','email','password')
        labels = {'username':"ユーザーID",'email':"メールアドレス"}


from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label#全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定する