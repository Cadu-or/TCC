import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

def graficos(ind1, ind2):
  series = pd.read_csv("tcc_app/static/tcc_app/csv/serie_2000a2021.csv")

  if ind1 != None and ind2 != None:
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
    fig.update_layout(paper_bgcolor="#FFFFFF", xaxis=dict(type='date'))

    # Salvar o gráfico em um arquivo HTML
    graph_html = pyo.plot(fig, output_type='div')
    
  else:
    fig = go.Figure()

    # Dados para o gráfico
    x_data = [1, 4, 4.5, 6, 8, 10, 12, 16, 18, 19, 22, 26, 27, 35]
    y_data = [1, 2, 1, 4, 1.2, 4.2, 6, 4.3, 5, 3.5, 6, 5.5, 4, 13]

    x_data2 = [1, 4, 4.5, 6, 8, 10, 12, 16, 18, 19, 22, 26, 27, 35]
    y_data2 = [10, 9, 12, 6, 9, 6, 10, 8, 9, 11, 12, 10, 14, 2]

    # Criar objeto de gráfico Scatter

    traco1 = go.Scatter(x=x_data, y=y_data, mode='lines', line=dict(color="#b2dafa"), showlegend=False)
    traco2 = go.Scatter(x=(x_data2), y=y_data2, mode='lines', line=dict(color="#ffbfb0"), showlegend=False)
  
    fig = go.Figure()

    fig.add_trace(traco1)
    fig.add_trace(traco2)

    # Adicionar anotação com seta
    fig.add_annotation(
      x=18,  # Posição x da anotação
      y=8,  # Posição y da anotação
      text='Selecione os indicadores',  # Texto da anotação
      ax=0,  # Deslocamento horizontal da anotação
      ay=0,  # Deslocamento vertical da anotação
      font=dict(
        family='Stick No Bills',  # Fonte do texto
        size=40,  # Tamanho da fonte do texto
        color='#BABABA'  # Cor do texto
      ),
    )

    # Configurar layout do gráfico
    fig.update_layout(
      plot_bgcolor='#FAFAFA',
      xaxis=dict(
        ticktext=[],  # Lista vazia para esconder os valores do eixo x
        tickvals=[]   # Lista vazia para esconder as marcações do eixo x
      ),
      yaxis=dict(
        ticktext=[],  # Lista vazia para esconder os valores do eixo x
        tickvals=[]   # Lista vazia para esconder as marcações do eixo x
      )
    )

    graph_html = pyo.plot(fig, output_type='div')
  
  return graph_html

def metadados(ind1, ind2):
  metadados = pd.read_csv("tcc_app/static/tcc_app/csv/metadados_mensal.csv")
  if ind1 != None and ind2 != None:
    df1 = metadados.query("CODE == @ind1").reset_index()
    df2 = metadados.query("CODE == @ind2").reset_index()

    print(list(df1['DESCRICAO'])[0])
    # CODE,DESCRICAO,GRANDE_TEMA,FONTE,MEDIDA
    indicador1 = {'code': list(df1['CODE'])[0], 
                  'descricao': list(df1['DESCRICAO'])[0], 
                  'medida': list(df1['MEDIDA'])[0],
                  'fonte': list(df1['FONTE'])[0],
                  'grande_tema': list(df1['GRANDE_TEMA'])[0]
                }
                 
    indicador2 = {'code': list(df2['CODE'])[0], 
                  'descricao': list(df2['DESCRICAO'])[0], 
                  'medida': list(df2['MEDIDA'])[0],
                  'fonte': list(df2['FONTE'])[0],
                  'grande_tema': list(df2['GRANDE_TEMA'])[0]
                }
  else:
    indicador1 = None
    indicador2 = None

  return indicador1, indicador2