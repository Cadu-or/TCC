from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from tcc_app.forms import IndicadoresForm 
import requests
from .components import correlacao_numero, graficos, metadados, correlacoes, metadados_content

from .database import DatabaseConnection
from decouple import config

# Create your views here.
def home(request):
  form = IndicadoresForm()

  db = DatabaseConnection(
    dbname=config('DB_NAME'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
  )

  if request.method == 'POST':
    form = IndicadoresForm(request.POST)
    ind1 = form.data['Indicador1']
    ind2 = form.data['Indicador2']
    delay = int(form.data['Delay'])
    #print(delay)
    
    correlacao = correlacao_numero(ind1, ind2, delay, db)
    graph_html = graficos(ind1, ind2, delay)
    indicador1, indicador2 = metadados(ind1, ind2)
    tabela1, tabela2 = correlacoes(ind1, ind2, db)

  else:
    correlacao = correlacao_numero(None, None, None, db)
    graph_html = graficos(None, None, None)
    indicador1, indicador2 = metadados(None, None)
    tabela1, tabela2 = correlacoes(None, None, db)


  context = {'correlacao': correlacao, 'graph_html': graph_html, 'form':form, 'indicador1': indicador1, 'indicador2': indicador2, 'tabela1': tabela1, 'tabela2': tabela2}

  return render(request, "tcc_app/home.html", context=context)

def filter(request):
  filtro = request.GET.get('filtro')
  resultados = metadados_content(filtro)
  resultados_json = [{'CODE': r[0], 'DESCRICAO': r[1]} for r in resultados]
  resultados_json = {'resultados': resultados_json}
  #print(type(resultados_json))
  
  return JsonResponse(resultados_json)