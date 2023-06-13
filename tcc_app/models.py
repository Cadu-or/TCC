from django.db import models
import pandas as pd
# Create your models here.
class Correlacao(models.Model):
  code1 = models.CharField(max_length=255)
  code2 = models.CharField(max_length=255)
  correlacao = models.FloatField()
  delay = models.IntegerField()
