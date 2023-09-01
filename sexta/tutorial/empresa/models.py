from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=True, default='')
    idade = models.IntegerField()
    email = models.EmailField()