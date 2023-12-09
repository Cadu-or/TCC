from django import forms
import pandas as pd

dataset = pd.read_csv('tcc_app/static/tcc_app/csv/indicadores.csv')
choices = tuple()
choicesDelay = tuple()

for i in pd.unique(dataset['code']):
  auxiliar = ((i,i),)
  choices = choices + auxiliar


DELAY_CHOICES = []

delay_1 = []
delay_2 = []

for i in range(1, 13):
  delay_1.append(('I1_' + str(i), i))

for i in range(1, 13):
  delay_2.append(('I2_' + str(i), i))
  
  
DELAY_CHOICES = (('Indicador 1', tuple(delay_1)), ('Indicador 2', tuple(delay_2)))

DELAY_CHOICES = tuple(DELAY_CHOICES)

#print(choicesDelay)

class IndicadoresForm(forms.Form):
  Indicador1 = forms.ChoiceField(choices=(('label', 'Indicador 1'),) + choices, label="", required=True)
  Indicador2 = forms.ChoiceField(choices=(('label', 'Indicador 2'),) + choices, label="", required=True)
  Delay = forms.ChoiceField(choices=(('I_0',0),) + DELAY_CHOICES, label="", required=True)