from django.urls import path
from .views import accueil,logine

urlpatterns = [
    path('asse/',accueil,),
    path('logine/',logine),

]
