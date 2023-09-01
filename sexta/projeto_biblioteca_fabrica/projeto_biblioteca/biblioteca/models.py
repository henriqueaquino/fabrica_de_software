from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100, blank=True, default='')
    autor = models.CharField(max_length=100, blank=True, default='')
    preco = models.FloatField()
''