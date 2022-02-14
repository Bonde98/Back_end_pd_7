from django.db import models
#from django.contrib import admin
# Create your models here.
class Tabcontact(models.Model):
   
    name = models.CharField(max_length=25)
    prenom = models.CharField(max_length=30)
    number = models.IntegerField(max_length=40)
    Email = models.EmailField(max_length=200)
    photos = models.FileField(null=True,blank=True ,upload_to='photos')
    password = models.CharField(max_length=30)


    def __str__(self) :
        return f"{self.prenom } { self.name} " 
          

'''class TabcontactAdmin(admin.ModelAdmin):
    list_display = ('prenom','name','Email','number', 'password',)
    list_filter = ('name',)
    search_fields = ['name', 'number', ]'''



        