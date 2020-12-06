from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, help_text='nome da categoria')

    def __str__(self):
        return self.nome