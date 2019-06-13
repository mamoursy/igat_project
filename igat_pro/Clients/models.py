from django.db import models

# Create your models here.

class Client(models.Model):
    Nom = models.CharField(max_length=200)
    Organisme = models.CharField(max_length=300)
    TEL = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Adresse_Postale = models.CharField(max_length=200)
    Ville = models.CharField(max_length=200)

    def __string__(self):
        return self.Nom
