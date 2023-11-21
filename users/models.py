from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # champs supplémentaires ici si nécessaire
    bio = models.TextField("Biographie", blank=True)
    birth_date = models.DateField("Date de naissance", null=True, blank=True)
    # d'autres champs personnalisés ici

    def __str__(self):
        return self.username
