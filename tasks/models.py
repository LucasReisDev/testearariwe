from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    prazo = models.DateField(null=True, blank=True)
    descricao = models.TextField(blank=True)
    finalizada = models.BooleanField()
