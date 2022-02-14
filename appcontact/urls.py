

from django.urls import path

from .views import index ,contact ,about,detail,articles,detail_article,Creation_article, modifier_article,profile ,connexion,supprimer,login_views,inscription,inscrire

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("accueil/", index, name='index'),
    path("contact/",contact, name="contact"),
    path("about/",about , name="about"),
    path("page_2/",articles , name='articles'),
    path("page_3/",detail_article, name='page_detail'),
    path("page_4/",Creation_article, name= "creation_article"),
    path("page_5/",modifier_article, name= "modifier_article"),
    path("page_8/",profile, name= "profile"),
    path("page_9/",connexion, name= "connexion"),
    path("page_10/",inscription, name= "inscription"),
    path("page_11/",supprimer, name= "supprimer"),
    path("detail/<int:id>",detail, name="detail"),
    path('login/',login_views,name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('inscrire/',inscrire,name="inscrire")
]