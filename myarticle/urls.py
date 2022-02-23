
from django.urls import path
from .views import accueil,les_articles, les_details_articles,delete_article,logine,p_article,dt_article,new_article,edit_article,my_contact,about,profile,asse

#importer fonction deconnnexion
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('art_accueil/',accueil,name="accueil_art"),
    path("page_2/",les_articles , name='articles'),
    path("page_3/",les_details_articles, name='page_detail'),
    path('logine/',logine,name="logine_art"),
    #path('inscrire/',inscription,name="inscrire"),
    path('article/',p_article,name="article_art"),
    path('details/<int:id>',dt_article,name="details"),
    path('new_article/',new_article,name="new_article"),
    path('edit/<int:id>',edit_article,name="edit"),
    path('delete/<int:id>',delete_article,name="delete"),
    path("contact/",my_contact, name="contact"),
    path("about/",about , name="about"),
    path("page_8/",profile, name= "profile"),
    path("asse/",asse, name= "asse"),
    path("logout/",LogoutView.as_view, name= "logout"),
]

