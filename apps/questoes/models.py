from django.db import models


# Create your models here.
from apps.categorias.models import Categoria


class Questoes(models.Model):
    RESPOSTA = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C')
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    pergunta = models.CharField(max_length=300, help_text='pergunta')
    alternativa_a = models.CharField(max_length=300, help_text='aternativa a')
    alternativa_b = models.CharField(max_length=300, help_text='aternativa b')
    alternativa_c = models.CharField(max_length=300, help_text='aternativa c')
    resposta = models.CharField(choices=RESPOSTA, max_length=1)


    def __str__(self):
        return self.pergunta