from django import forms
import pandas as pd

dataset = pd.read_csv('tcc_app/static/tcc_app/csv/codigos_correlacao_mensal.csv')
choices = tuple()

for i in pd.unique(dataset['CODE']):
  auxiliar = ((i,i),)
  choices = choices + auxiliar

class IndicadoresForm(forms.Form):
  Indicador1 = forms.ChoiceField(choices=choices, label="")
  Indicador2 = forms.ChoiceField(choices=choices, label="")