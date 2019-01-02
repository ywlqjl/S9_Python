from django.db import models
import hashlib

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=500)

class User(models.Model):
    username = models.CharField(max_length=30, default="admin")
    password = models.TextField(default=hashlib.sha3_256(b"password").hexdigest())

    def __unicode__(self):
        return self.username