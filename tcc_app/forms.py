from django import forms
import pandas as pd

dataset = pd.read_csv('tcc_app/static/tcc_app/csv/indicadores.csv')
choices = tuple()
choicesDelay = tuple()

for i in pd.unique(dataset['code']):
  auxiliar = ((i,i),)
  choices = choices + auxiliar

for i in range(-12,13):
  auxiliar = ((i,i),)
  choicesDelay = choicesDelay + auxiliar

#print(choicesDelay)

class IndicadoresForm(forms.Form):
  Indicador1 = forms.ChoiceField(choices=(('label', 'Indicador 1'),) + choices, label="", required=True)
  Indicador2 = forms.ChoiceField(choices=(('label', 'Indicador 2'),) + choices, label="", required=True)
  Delay = forms.ChoiceField(choices=(('label', 'Delay',),) + choicesDelay, label="", required=True)