
from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=40)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.ism}"

class Albom(models.Model):
    nom = models.CharField(max_length=100)
    sana = models.DateField(null=True, blank=True)
    rasm = models.URLField(blank=True, null=True)
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}"

class Qoshiq(models.Model):
    nom = models.CharField(max_length=100)
    janr = models.CharField(max_length=100)
    sana = models.DateField()
    fayl = models.FileField()
    davomiylik = models.DurationField()
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.nom}"

