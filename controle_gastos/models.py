from django.db import models

class despesas(models.Model):
    valor = models.IntegerField()
    data = models.DateField
    categoria = models.CharField(max_length=200)
    descricao = models.TextField()

    def __str__(self):
        return self.categoria
    
