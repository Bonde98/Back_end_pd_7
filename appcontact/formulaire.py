


from django.forms import ModelForm 
from django import forms
from .models import Tabcontact

class TabcontactForm(forms.ModelForm):
    class Meta:
        # Préciser le model utiliser
        model = Tabcontact
        # Les champs a affichers
        fields = ('prenom','name','number' ,'Email' ,'password', 'photos')
        labels = {
                'prenom':"Prenom d'utilisteur ",
                'name':"Nom d'utilisateur",
                'number':"Numéro de Téléphone",
                'Email':"Email",
                'password':"Mot de Passe",
                'photos':"Photos"
                }
        Widget = {
                
                "prenom":forms.TextInput(attrs ={'class':" form-control"}),
                'name': forms.TextInput(attrs={'class':"form-control"}),
                'number':forms.TextInput (attrs={'class':"form-control"}),
                'Email':forms.EmailInput(attrs={'class':"form-control"}),
                'password':forms.PasswordInput(attrs={'class':"form-control",}),
                'photos':forms.FileInput(attrs={'class':"form-control"}),
                }





class inscrireForm(forms.Form):
        
                
                name = forms.CharField(label="Nom d'utilisateur",
                                        widget=forms.TextInput
                                        (attrs={"class":"form-control"} ))
                prenom = forms.CharField(label="Prenom d'utilisateur",
                                        widget=forms.TextInput
                                        (attrs={"class":"form-control"} ))
        
                Email = forms.EmailField(label="Email",
                                        widget=forms.TextInput
                                        (attrs={"class":"form-control"} ))

                number = forms.IntegerField(label="Numéro-Téléphone" , 
                                        widget =forms.NumberInput
                                                ( attrs={ "class":"form-control"} ))
                password = forms.CharField(label="Mot de Passe" , 
                                        widget =forms.PasswordInput
                                                ( attrs={ "class":"form-control"} ))


'''photos = forms.FileField(label="Photos" , 
                                        widget =forms.FileInput
                                                ( attrs={ "class":"form-control"} ))'''

                

class loginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur",
                                 widget=forms.TextInput
                                (attrs={"class":"form-control"} ))

    password = forms.CharField(label="Mot de Passe" , 
                                widget =forms.PasswordInput
                                        ( attrs={ "class":"form-control"} ))
    
    