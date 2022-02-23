from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# table model article
class article(models.Model):
    titre = models.CharField(max_length=25)
    resume = models.CharField(max_length=250)
    photos = models.FileField(null=True,blank=True,upload_to='photos')
    contenu = models.CharField(max_length=1000)
    Auteur = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    dt_creation = models.DateTimeField(auto_now_add=True)
    dr_mise_jr = models.DateTimeField(auto_now_add=True)
    archive = models.BooleanField(default=False)
    def __str__(self) :
        return f" L'auteur: {self.Auteur} Titre: {self.titre}"