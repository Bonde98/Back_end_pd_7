

from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render ,get_object_or_404
from .models import Tabcontact 
from .formulaire import  loginForm,TabcontactForm,inscrireForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.
from django.contrib.auth.decorators import login_required

def inscription(request):
    if request.method == "POST":
        form = TabcontactForm(request.POST,request.FILES).save()   
        return HttpResponseRedirect('/page_9')
    else:
        form = TabcontactForm()
    return render(request,"page/10_inscription.html",{'form':form})



def index(request):
    return render(request ,"page/index.html")

@login_required(login_url="/login/")
def contact (request):
    contacts = Tabcontact.objects.all()
    return render(request ,"page/contact.html",{"contacts" :contacts})


def about (request):
    return render(request ,"page/about.html")

@login_required(login_url="/login/")
def contact_details (request , id):
    contacts = get_object_or_404(Tabcontact, id=id)
    return render(request,"page/10_inscription.html",{"contacts":contacts})

def articles(request):
    return render(request,"page/2_les_articles.html")



def detail_article(request):
    return render(request,"page/3_detail_article.html")

@login_required(login_url="/login/")
def Creation_article(request):
    return render(request,"page/4_creation_article.html")

@login_required(login_url="/login/")
def modifier_article(request):
    return render(request,"page/5_modifier_article.html")

def profile(request):
    return render(request,"page/8_profile.html")

def connexion(request):
    return render(request,"page/9_connexion.html")



@login_required(login_url="/login/")
def supprimer(request):
    return render(request,"page/11_supprimer.html")

@login_required(login_url="/login/")
def detail(request,id):
    contact = get_object_or_404(Tabcontact, id=id)
    return render(request,"page/detail.html",{'contact':contact})

def login_views(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/accueil")
    return render(request,"page/login.html",{'form':form})



def inscrire(request):
    inscrit = inscrireForm(request.POST or None)
    if inscrit.is_valid():
        username = inscrit.cleaned_data.get("prenom")
        w_password = inscrit.cleaned_data.get("password")
        user = authenticate(username=username,password=w_password)
        if User is not None:
            login(request,user)
            return redirect("/login")
    return render(request,"page/inscrire.html",{'inscrit':inscrit})

