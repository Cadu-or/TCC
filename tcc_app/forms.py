from django import forms
import pandas as pd

dataset = pd.read_csv('tcc_app/static/tcc_app/csv/9-filtro_serie_mensal_completa.csv')
choices = tuple()
choicesDelay = tuple()

for i in pd.unique(dataset['CODE']):
  auxiliar = ((i,i),)
  choices = choices + auxiliar

for i in range(-12,13):
  auxiliar = ((i,i),)
  choicesDelay = choicesDelay + auxiliar

#print(choicesDelay)

class IndicadoresForm(forms.Form):
  Indicador1 = forms.ChoiceField(choices=choices, label="")
  Indicador2 = forms.ChoiceField(choices=choices, label="")
  Delay = forms.ChoiceField(choices=choicesDelay, label="")