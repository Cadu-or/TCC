from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from tcc_app.forms import IndicadoresForm 
import requests
from .components import correlacao_numero, graficos, metadados, correlacoes, metadados_content

# Create your views here.
def home(request):
  form = IndicadoresForm()
  condicao = False
  if request.method == 'POST':
    form = IndicadoresForm(request.POST)
    ind1 = form.data['Indicador1']
    ind2 = form.data['Indicador2']
    delay = int(form.data['Delay'])
    print(delay)
    
    correlacao = correlacao_numero(ind1, ind2, delay)
    graph_html = graficos(ind1, ind2, delay)
    indicador1, indicador2 = metadados(ind1, ind2)
    tabela1, tabela2 = correlacoes(ind1, ind2)

  else:
    correlacao = correlacao_numero(None, None, None)
    graph_html = graficos(None, None, None)
    indicador1, indicador2 = metadados(None, None)
    tabela1, tabela2 = correlacoes(None, None)


  print(indicador1)
  print(indicador2)
  context = {'correlacao': correlacao, 'graph_html': graph_html, 'form':form, 'indicador1': indicador1, 'indicador2': indicador2, 'tabela1': tabela1, 'tabela2': tabela2, 'condicao': condicao }
  
  return render(request, "tcc_app/home.html", context=context)

def filter(request):
  filtro = request.GET.get('filtro')
  resultados = metadados_content(filtro)
  resultados_json = [{'CODE': r[0], 'DESCRICAO': r[1]} for r in resultados]
  resultados_json = {'resultados': resultados_json}
  print(type(resultados_json))
  
  return JsonResponse(resultados_json)