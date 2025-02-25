from django.db import models
class Correlacao(models.Model):
  code1 = models.CharField(max_length=255)
  code2 = models.CharField(max_length=255)
  correlacao = models.FloatField()
  delay = models.IntegerField()
