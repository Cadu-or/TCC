from django.shortcuts import render
from tcc_app.forms import IndicadoresForm 

import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Create your views here.
def home(request):
  form = IndicadoresForm()
  series = pd.read_csv("tcc_app/static/tcc_app/csv/serie_2000a2021.csv")
  metadados = pd.read_csv("tcc_app/static/tcc_app/csv/metadados_mensal.csv")

  if request.method == 'POST':
    form = IndicadoresForm(request.POST)
    ind1 = form.data['Indicador1']
    ind2 = form.data['Indicador2']

    df1 = series.query("CODE == @ind1").reset_index()
    df2 = series.query("CODE == @ind2").reset_index()

    fig = go.Figure()
    
    df1['data'] = pd.to_datetime(df1[['YEAR', 'MONTH']].assign(day=1))
    df2['data'] = pd.to_datetime(df2[['YEAR', 'MONTH',]].assign(day=1))

    traco1 = go.Scatter(x=df1["data"], y=df1["VALUE"], name=ind1, yaxis='y')
    traco2 = go.Scatter(x=df2["data"], y=df2["VALUE"], name=ind2, yaxis='y2')

    fig.add_trace(traco1)
    fig.add_trace(traco2)

    layout = go.Layout(title='Gráfico com Dois Indicadores')

    fig.update_layout(yaxis=dict(title=ind1))
    fig.update_layout(yaxis2=dict(title=ind2, overlaying='y', side='right'))

    # Criar o objeto de gráfico
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", xaxis=dict(type='date'))

    # Salvar o gráfico em um arquivo HTML
    graph_html = pyo.plot(fig, output_type='div')
  else:
    fig = go.Figure()

    # Constants
    img_width = 1600
    img_height = 900
    scale_factor = 0.5

    # Add invisible scatter trace.
    # This trace is added to help the autoresize logic work.
    fig.add_trace(
      go.Scatter(
        x=[0, img_width * scale_factor],
        y=[0, img_height * scale_factor],
        mode="markers",
        marker_opacity=0
      )
    )

    # Configure axes
    fig.update_xaxes(
      visible=False,
    )

    fig.update_yaxes(
      visible=False,
      scaleanchor="x"
    )

    # Add image
    fig.add_layout_image(
      dict(
        sizex=img_width * scale_factor,
        y=img_height * scale_factor,
        sizey=img_height * scale_factor,
        xref="x",
        yref="y",
        opacity=1.0,
        layer="below",
        sizing="stretch",
        source="/static/tcc_app/GraficoDosindicadores.png"
      )
    )

    # Configure other layout
    fig.update_layout(
      margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )

    graph_html = pyo.plot(fig, output_type='div')

  context = {'graph_html': graph_html, 'form':form}

  return render(request, "tcc_app/home.html", context=context)