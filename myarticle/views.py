from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
def accueil(request):
    return render(request,'articles/accueil.html')

def logine(request):
    forme = LoginForm
    return render(request,"articles/logine.html",{'forme':forme})