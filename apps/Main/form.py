from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post,Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput)
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']
        help_texts = {k: "" for k in fields}

class PostForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={
        'placeholder':'¿Que esta pasando?',
        }))
    
    class Meta:
        model=Post
        fields=['content']


class EditProfileForm(forms.ModelForm):
    portada = forms.FileField(label='Portada', widget=forms.FileInput)
    image = forms.FileField(label='Foto', widget=forms.FileInput)
    biografia = forms.CharField(label='Biografia', widget= forms.TextInput)
    social = forms.CharField(label='Web', widget=forms.TextInput)
    
    class Meta:
        model = Profile
        fields = ['portada','image','biografia','social']