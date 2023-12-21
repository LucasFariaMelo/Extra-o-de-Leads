from django.db import models

# Create your models here.

class Lead(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, default='Topo de Funil')

    def __str__(self):
        return self.nome