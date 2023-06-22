from django.shortcuts import render
from tcc_app.forms import IndicadoresForm 
from .components import correlacao_numero, graficos, metadados, correlacoes

# Create your views here.
def home(request):
  form = IndicadoresForm()
  
  if request.method == 'POST':
    form = IndicadoresForm(request.POST)
    ind1 = form.data['Indicador1']
    ind2 = form.data['Indicador2']
    
    correlacao = correlacao_numero(ind1, ind2)
    graph_html = graficos(ind1, ind2)
    indicador1, indicador2 = metadados(ind1, ind2)
    tabela1, tabela2 = correlacoes(ind1, ind2)

  else:
    
    correlacao = correlacao_numero(None, None)
    graph_html = graficos(None, None)
    indicador1, indicador2 = metadados(None, None)
    tabela1, tabela2 = correlacoes(None, None)

  context = {'correlacao': correlacao, 'graph_html': graph_html, 'form':form, 'indicador1': indicador1, 'indicador2': indicador2, 'tabela1': tabela1, 'tabela2': tabela2}

  return render(request, "tcc_app/home.html", context=context)