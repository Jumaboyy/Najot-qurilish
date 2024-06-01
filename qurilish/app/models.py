# blog/models.py

from django.db import models

class Hudud(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class QurilishTashkiloti(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    qachon_tashkil_topgan = models.DateField()
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE, related_name='tashkilotlar')

    def __str__(self):
        return self.name

class QurilishBinisi(models.Model):
    qurilish_tashkiloti = models.ForeignKey(QurilishTashkiloti, on_delete=models.CASCADE, related_name='binolar')
    hudud = models.ForeignKey(Hudud, on_delete=models.CASCADE, related_name='binolar')
    name = models.CharField(max_length=100)
    maydoni = models.FloatField()
    qavat = models.IntegerField()
    parkovka = models.BooleanField(default=False)
    bolalar_maydonchasi = models.BooleanField(default=False)
    lift = models.BooleanField(default=False)

    def __str__(self):
        return self.name
