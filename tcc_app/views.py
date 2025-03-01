from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from tcc_app.forms import IndicadoresForm 
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
    delay = form.data['Delay']
    if(str(delay[:2]) == 'I2'):
      delay = int(delay[3:])
    elif(str(delay[:2]) == 'I1'):
      delay = int(delay[3:]) * -1
    else:
      delay = 0

    correlacao = correlacao_numero(ind1, ind2, delay, db)
    graph_html = graficos(ind1, ind2, delay)
    indicador1, indicador2 = metadados(ind1, ind2)
    tabela1, tabela2 = correlacoes(ind1, ind2, db)

  else:
    correlacao = correlacao_numero(None, None, None, db)
    graph_html = graficos(None, None, None)
    indicador1, indicador2 = metadados(None, None)
    tabela1, tabela2 = correlacoes(None, None, db)
    delay = None

  context = {'correlacao': correlacao, 'graph_html': graph_html, 'form':form, 'indicador1': indicador1, 'indicador2': indicador2, 'tabela1': tabela1, 'tabela2': tabela2, 'delay': delay}
  
  return render(request, "tcc_app/home.html", context=context)

def filter(request):
  filtro = request.GET.get('filtro')
  resultados = metadados_content(filtro)
  resultados_json = [{'CODE': r[0], 'DESCRICAO': r[1]} for r in resultados]
  resultados_json = {'resultados': resultados_json}

  return JsonResponse(resultados_json)

def filterhome(request, indicador1=None, indicador2=None, delay=None):
  delayInt = int(delay)
  form = IndicadoresForm()

  db = DatabaseConnection(
    dbname=config('DB_NAME'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD'),
    host=config('DB_HOST'),
  )

  if indicador1 is not None and indicador2 is not None:
    form.data['Indicador1'] = indicador1
    form.data['Indicador1'] = indicador2
    form.data['Delay'] = delayInt
    
    correlacao = correlacao_numero(indicador1, indicador2, delayInt, db)
    graph_html = graficos(indicador1, indicador2, delayInt)

    indic1, indic2 = metadados(indicador1, indicador2)

    tabela1, tabela2 = correlacoes(indicador1, indicador2, db)

    
  else:
    correlacao = None
    graph_html = None

    indic1, indic2 = None, None

    tabela1, tabela2 = None, None
  
  context = {'correlacao': correlacao, 'graph_html': graph_html, 'form':form, 'indicador1': indic1, 'indicador2': indic2, 'tabela1': tabela1, 'tabela2': tabela2, 'delay': delayInt }

  return render(request, "tcc_app/home.html", context=context)