from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CartaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    tipo = forms.CharField(max_length=100, required=True)

class FiguraForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    material = forms.CharField(max_length=100, required=True)    

class DibujoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    autor = forms.CharField(max_length=100, required=True)    

class RegistroForm(UserCreationForm): 
    email = forms.EmailField(required=True)   
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma Contraseña", widget=forms.PasswordInput)    

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class CamisetaForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    color = forms.CharField(max_length=100, required=True)  
    forma = forms.CharField(max_length=100, required=True)  

class UserEditForm(UserChangeForm): 
    email = forms.EmailField(required=True)   
    first_name = forms.CharField(label="Nombre/s", max_length=100, required=True)
    last_name = forms.CharField(label="Apellido/s", max_length=100, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]    

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)       
