
from xml.parsers.expat import model
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LogineForm(forms.Form):
    Username = forms.CharField(label = "Nom d'utilisateur",
                                 widget= forms.TextInput 
                                (attrs={"class":"form-control"}))
                                
    password = forms.CharField(label = "Mot de passe",
                                widget= forms.PasswordInput
                                (attrs={"class":"form-control"}))

class Signupform(UserCreationForm):
    username = forms.CharField(label = "Nom d'utilisateur",
                                        widget= forms.TextInput 
                                        (attrs={"class":"form-control"}))
    Email = forms.EmailField(label = "Email",
                                        widget= forms.TextInput 
                                        (attrs={"class":"form-control"}))
                                        
    password1 = forms.CharField(label = "Mot de passe",
                                        widget= forms.PasswordInput
                                        (attrs={"class":"form-control"}))
    password2 = forms.CharField(label = "Confirmer Mot de passe",
                                        widget= forms.PasswordInput
                                        (attrs={"class":"form-control"}))
    class Meta:
        model= User
        fields = ('username','Email','password1','password2')



