from django import forms
from app1.models import Blog
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'

class EditForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'