from django.db import models
from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    matn = models.CharField(max_length=500)
    rasm = models.FileField()

class Intervyu(models.Model):
    sarlavha = models.CharField(max_length=50)
    sana = models.DateField()
    video = models.CharField(max_length=300)