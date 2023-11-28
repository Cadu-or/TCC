import pandas as pd;

ind = 142581429

correlacao = pd.read_csv("3-correlacao_mensal_completa.csv")
colunas = ['id', 'code1', 'code2', 'delay', 'correlation']
csvfinal = pd.DataFrame(columns=colunas)

for i, j in correlacao.iterrows():
    print(i)
    ind = ind+1
    nova_linha = pd.DataFrame([[ind, j['CODE1'], j['CODE2'], 0, round(j['CORRELATION'], 3)]], columns=colunas)
    csvfinal = pd.concat([csvfinal, nova_linha], ignore_index=True)

csvfinal.to_csv('correlacao0.csv')
