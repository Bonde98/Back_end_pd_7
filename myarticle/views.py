
from django.shortcuts import redirect, render,get_object_or_404
from .forms import LogineForm,SignUpForm
from .models import article
from django.contrib.auth  import authenticate ,login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def accueil(request):
    return render(request,'articles/accueil.html')


def les_articles(request):
    return render(request,"articles/2_les_articles.html")

def about(request):
    return render(request,"articles/about.html")

def my_contact(request):
    return render(request,"articles/contact.html")

def profile(request):
    return render(request,"articles/8_profile.html")

def les_details_articles(request):
    return render(request,"articles/3_detail_article.html")
#connexion
def logine(request):
    forme = LogineForm(request.POST or None)
    if forme.is_valid():
        username = forme.cleaned_data.get("Username") 
        password = forme.cleaned_data.get("password") 
        user = authenticate(request,username=username,password=password)
        if user is not None:
           login(request,user)
           return redirect("/art_accueil/")
    
    return render(request,"articles/logine.html",{'forme':forme})

#inscription
'''def inscription(request):
    if request.method == "POST":
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/logine/")
    else:
        form = Signupform()
        return redirect("/inscrire/")
    return render(request,"articles/inscription.html",{'form':form})'''

#Page des articles
@login_required(login_url="/logine/")
def p_article(request):
    user = request.user
    v_article = article.objects.filter(Auteur=user,archive=False)
    return render(request,"articles/p_articles.html",{'v_article':v_article})

#Page details d' article
@login_required(login_url="/logine/")
def dt_article(request,id):
    detaille = get_object_or_404(article,id=id)
    return render(request,"articles/dtl_article.html",{'detaille':detaille})

#Nouveau article
@login_required(login_url="/logine/")
def new_article(request):
    if request.method == "POST":
      Auteur = request.user
      titre = request.POST['titre']
      resume = request.POST['resume']
      photos = request.FILES['photos']
      contenu = request.POST['contenu']
      articles = article.objects.create(
          Auteur=Auteur,
          titre=titre,
          resume=resume,
          photos=photos,
          contenu=contenu,

      )
      articles.save()
      return redirect("/article/")

    return render(request,"articles/new_article.html")


#Modifier article
@login_required(login_url="/logine/")
def edit_article(request,id):
    articles = get_object_or_404(article, id=id)
    if request.method == "POST":
      titre = request.POST['titre']
      resume = request.POST['resume']
      photos = request.POST['photos']
      contenu = request.POST['contenu']
      articles = article.objects.filter(pk= id)
      articles.update(
          titre=titre,
          resume=resume,
          photos=photos,
          contenu=contenu,
      ) 
      return redirect("/article/")
    
    return render(request,"articles/edit_article.html",{"articles":articles})


#Supprimer article
@login_required(login_url="/logine/")
def delete_article(request,id):
    articles = get_object_or_404(article, id=id)
    if request.method == "POST":
       articles = article.objects.filter(pk= id)
       articles.update(
           archive=True
       )
       return redirect("/article/")
    
    return render(request,"articles/delete_article.html",{"articles":articles})


'''def asse(request):
    if request.method == "POST":
        asse = Signupform(request.POST)    
        if asse.is_valid():
            asse.save()
            username = asse.cleaned_data.get("username")
            raw_password = asse.cleaned_data.get("password1")
            user = authenticate(username=username,password=raw_password)
            return redirect("/logine/")
    else:
        asse = Signupform()
        return redirect("/asse/")
    return render(request,"articles/asse.html",{'asse':asse})
    '''

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/logine/")
    else:
        form = SignUpForm()
    return render(request, "articles/asse.html", {"form": form})