import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from dateutil.relativedelta import relativedelta
import time

def correlacao_numero(ind1, ind2, delay, db):
  if ind1 != None and ind2 != None:
    result1 = db.execute_query(f"SELECT correlation FROM dbo.tb_correlacao WHERE code1 = '{ind1}' AND code2 = '{ind2}' AND delay = {delay}")
    result2 = db.execute_query(f"SELECT correlation FROM dbo.tb_correlacao WHERE code1 = '{ind2}' AND code2 = '{ind1}' AND delay = {delay}")

    if result1:
      correlacao = float(result1[0][0])
    elif result2:
      correlacao = float(result2[0][0])
    else: 
      correlacao = None
  else:
    correlacao = None


  return correlacao


def graficos(ind1, ind2, delay):
  series = pd.read_csv("tcc_app/static/tcc_app/csv/9-filtro_serie_mensal_completa.csv")

  if ind1 != None and ind2 != None:
    df1 = series.query("CODE == @ind1").reset_index()
    df2 = series.query("CODE == @ind2").reset_index()

    fig = go.Figure()
      
    df1['data'] = pd.to_datetime(df1[['YEAR', 'MONTH']].assign(day=1))
    df2['data'] = pd.to_datetime(df2[['YEAR', 'MONTH',]].assign(day=1))

    for y in range(df2['data'].size):
      if(delay >= 0):
        df2['data'][y] = df2['data'][y] + relativedelta(months=delay)
      else:
        df1['data'][y] = df1['data'][y] + relativedelta(months=abs(delay))
    for y in range(abs(delay)):
      if(delay >= 0):
        index_of_last_item = df2['data'].index[-1]
        df2 = df2.drop(index_of_last_item)
      else:
        index_of_last_item = df1['data'].index[-1]
        df1 = df1.drop(index_of_last_item)

      
    traco1 = go.Scatter(x=df1["data"], y=df1["VALUE"], name=ind1, yaxis='y')
    traco2 = go.Scatter(x=df2["data"], y=df2["VALUE"], name=ind2, yaxis='y2')

    fig.add_trace(traco1)
    fig.add_trace(traco2)

    layout = go.Layout(title='Gráfico com Dois Indicadores')

    fig.update_layout(yaxis=dict(title=ind1), legend=dict(x=-0, y=1.2))
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
      )
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
  metadados = pd.read_csv("tcc_app/static/tcc_app/csv/metadados_mensal_completa.csv")
  if ind1 != None and ind2 != None:
    df1 = metadados.query("CODE == @ind1").reset_index()
    df2 = metadados.query("CODE == @ind2").reset_index()

    #print(list(df1['DESCRICAO'])[0])
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


def correlacoes(ind1, ind2, db):
  if ind1 != None and ind2 != None:
    table1 = pd.DataFrame(columns=['Codigo', 'Delay', 'Correlação'])
    table2 = pd.DataFrame(columns=['Codigo', 'Delay', 'Correlação'])

    df1asc = db.execute_query(f"SELECT TOP 10 correlation, code1, code2, delay FROM dbo.tb_correlacao WHERE code1 = '{ind1}' or code2 = '{ind1}' ORDER BY correlation ASC")
    df1desc = db.execute_query(f"SELECT TOP 10 correlation, code1, code2, delay FROM dbo.tb_correlacao WHERE code1 = '{ind1}' or code2 = '{ind1}' ORDER BY correlation DESC")

    df1 = pd.concat([df1asc, df1desc])

    df2asc = db.execute_query(f"SELECT TOP 10 correlation, code1, code2, delay FROM dbo.tb_correlacao WHERE code1 = '{ind2}' or code2 = '{ind2}' ORDER BY correlation ASC")
    df2desc = db.execute_query(f"SELECT TOP 10 correlation, code1, code2, delay FROM dbo.tb_correlacao WHERE code1 = '{ind2}' or code2 = '{ind2}' ORDER BY correlation DESC")

    df2 = pd.concat([df2asc, df2desc])

    for i, j in df1.iterrows():
      if j['CODE1'] == ind1:
        table1 = pd.concat([table1, pd.DataFrame({'Codigo': [j['CODE2']], 'Delay': [j['DELAY']], 'Correlação': [j['CORRELATION']]})], ignore_index=True)
      else:
        table1 = pd.concat([table1, pd.DataFrame({'Codigo': [j['CODE1']], 'Delay': [j['DELAY']], 'Correlação': [j['CORRELATION']]})], ignore_index=True)
    
    for i, j in df2.iterrows():
      if j['CODE1'] == ind2:
        table2 = pd.concat([table2, pd.DataFrame({'Codigo': [j['CODE2']], 'Delay': [j['DELAY']], 'Correlação': [j['CORRELATION']]})], ignore_index=True)
      else:
        table2 = pd.concat([table2, pd.DataFrame({'Codigo': [j['CODE1']], 'Delay': [j['DELAY']], 'Correlação': [j['CORRELATION']]})], ignore_index=True)
    
    table1 = table1.sort_values(by=['Correlação'], ascending=False)
    table2 = table2.sort_values(by=['Correlação'], ascending=False)

    tabela_plot = go.Table(
            header=dict(values=list(table1.columns),
                        fill_color='#b2dafa',
                        align='center'),
            cells=dict(values=[table1.Codigo, table1.Delay, table1.Correlação],
                      fill_color='white',
                      align='center'))
    
    tabela2_plot = go.Table(
            header=dict(values=list(table2.columns),
                        fill_color='#ffbfb0',
                        align='center'),
            cells=dict(values=[table2.Codigo, table2.Delay, table2.Correlação],
                      fill_color='white',
                      align='center'))

    fig = go.Figure(data=tabela_plot)
    fig2 = go.Figure(data=tabela2_plot)

    fig.update_layout(
      margin=dict(l=0, r=0, t=0, b=0),
      plot_bgcolor='rgba(0,0,0,0)',   # Definir o fundo do gráfico como transparente
      showlegend=False,               # Ocultar a legenda
      width=375,
      height=375,
      font=dict(
        family='Inter',  # Fonte do texto
        size=10,  # Tamanho da fonte do texto
      ),
    )

    fig2.update_layout(
      margin=dict(l=0, r=0, t=0, b=0),
      plot_bgcolor='rgba(0,0,0,0)',   # Definir o fundo do gráfico como transparente
      showlegend=False,               # Ocultar a legenda
      width=375,
      height=375,
      font=dict(
        family='Inter',  # Fonte do texto
        size=10,  # Tamanho da fonte do texto
      ),
    )

    table1 = pyo.plot(fig, output_type='div')
    table2 = pyo.plot(fig2, output_type='div')

  else:
    table1, table2 = None, None

  return table1, table2

def metadados_content(filtro):
  metadados = pd.read_csv("tcc_app/static/tcc_app/csv/metadados_mensal_completa.csv")
  if filtro:
    dataset = metadados.query('DESCRICAO.str.contains(@filtro, case=False)')
    dataset = dataset[['CODE', 'DESCRICAO']].values.tolist()
  else:
    dataset = metadados[['CODE', 'DESCRICAO']].values.tolist()

  return dataset