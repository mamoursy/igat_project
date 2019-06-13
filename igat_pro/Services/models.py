from django.db import models

# Create your models here.

class Service(models.Model):
    Types_de_services = models.CharField(max_length=300)
    Expertise = models.CharField(max_length=300)

    def __string__(self):
        return self.Types_de_services
