from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import user_table

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',max_length=150)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not user_table.objects.filter(name=username).exists():
            raise forms.ValidationError('Invalid Username')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = user_table.objects.filter(name=username).first()
            if user and not user.check_password(password):
                raise forms.ValidationError('Invalid Password')
        return cleaned_data
