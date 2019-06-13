from django.db import models
from Clients.models import Client
from datetime import datetime

# Create your models here.

class Formation(models.Model):
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    Mode_de_formation = models.CharField(max_length=200)
    Types_de_formation = models.CharField(max_length=200)
    Durée = models.DurationField()

    def __string__(self):
        return self.Client
