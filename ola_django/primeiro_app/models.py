from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=45)
    idade = models.IntegerField()
    email = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.nome
