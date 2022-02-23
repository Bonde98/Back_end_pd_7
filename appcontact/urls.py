

from django.urls import path

from .views import index 
#login_views

#rom django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accueil/", index, name='index'),
    
    
    #path("page_4/",Creation_article, name= "creation_article"),
    #path("page_5/",modifier_article, name= "modifier_article"),
    
    #path("page_9/",connexion, name= "connexion"),
    #path("page_10/",inscription, name= "inscription"),
    #path("page_11/",supprimer, name= "supprimer"),
    #path("detail/<int:id>",detail, name="detail"),
    #path('login/',login_views,name="login"),
    #path('logout/',LogoutView.as_view(),name="logout"),
    #path('inscrire/',inscrire,name="inscrire")
]