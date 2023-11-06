import pandas as pd
import numpy as np
import datetime
from numba import jit

def delay_correlation(x, y, delay):
    n = len(x)
    correlation = np.corrcoef(x[:n-delay], y[delay:])[0, 1]
    return correlation

def loop_acelerado(arq, arq2):
    lista_corr_mensal_delay = arq.values.tolist()
    lista_final = []
    j = 0
    for i in lista_corr_mensal_delay:
        d1 = arq2.query("CODE == @i[0]").reset_index()
        d2 = arq2.query("CODE == @i[1]").reset_index()
        print(j)
        for k in range(1,13):
            correlation = delay_correlation(d1['VALUE'], d2['VALUE'], k)
            corr_mensal_delay_new_row = [i[0], i[1], correlation, k]
            lista_final.append(corr_mensal_delay_new_row)
        j = j + 1
    
    corr_mensal_delay = pd.DataFrame(lista_final, columns=['CODE1', 'CODE2', 'CORRELATION', 'DELAY'])
    corr_mensal_delay.to_csv("corr_mensal_delay_positivo_2.csv", index=False)

corr_mensal_teste = pd.read_csv('3-correlacao_mensal_completa.csv')
serie_mensal_completa = pd.read_csv('9-filtro_serie_mensal_completa.csv')

loop_acelerado(corr_mensal_teste, serie_mensal_completa)
