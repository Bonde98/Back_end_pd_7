# Generated by Django 4.0.3 on 2022-03-10 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=25)),
                ('resume', models.CharField(max_length=250)),
                ('photos', models.FileField(blank=True, null=True, upload_to='photos')),
                ('contenu', models.CharField(max_length=1000)),
                ('dt_creation', models.DateTimeField(auto_now_add=True)),
                ('dr_mise_jr', models.DateTimeField(auto_now_add=True)),
                ('archive', models.BooleanField(default=False)),
                ('Auteur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
