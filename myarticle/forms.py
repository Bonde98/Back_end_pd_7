from django import forms

class LogineForm(forms.Form):
    Username = forms.CharField()
    password = forms.CharField()
