from django.shortcuts import render
from tcc_app.forms import IndicadoresForm 
from .components import graficos, metadados

# Create your views here.
def home(request):
  form = IndicadoresForm()
  
  if request.method == 'POST':
    form = IndicadoresForm(request.POST)
    ind1 = form.data['Indicador1']
    ind2 = form.data['Indicador2']
    
    graph_html = graficos(ind1, ind2)
    indicador1, indicador2 = metadados(ind1, ind2)

  else:
    graph_html = graficos(None, None)
    indicador1, indicador2 = metadados(None, None)

  context = {'graph_html': graph_html, 'form':form, 'indicador1': indicador1, 'indicador2': indicador2}

  return render(request, "tcc_app/home.html", context=context)