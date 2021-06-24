import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## Carregamento da base de dados
def loadData():
    chunks = []
    for chunk in pd.read_csv('C:/Users/Ygoor/Desktop/Facul/LABS/dados_b.csv', encoding = 'UTF-8', sep = ',', low_memory = True, chunksize=1000):
        chunks.append(chunk)
    df = pd.concat(chunks)
    df = df.astype(float)
    return df

df= loadData()
x = df['tempo (s)']*(1/60)
y = df['pressao (mbar) dwyer digital (99 mL/min)']

## Função de otimização para curva exponencial em Q
def func(x,p1,p2):
    return p1*x + p2

## Otimização QxP
popt, pcov = curve_fit(func, x, y, p0 = (1, 0))
p1, p2 = popt
yfitted = func(x, *popt)

## Cálculo de parâmetros para QxP
media = y.mean()
dp = y.std()
var = y.var()
corr = y.corr(x)
print('')
print(p1,'.x + ',p2)
print('Pressão Média: ', media)
print('Desvio padrão: ', dp)
print('Variância: ', var)
print('Corr: ', corr)

## Cálculo do Volume
P0 = df.iloc[0,1]
tm = x.mean()
Q = 99
P = media
V = Q*tm/P-P0
print('Volume Médio = ',V)
## Gráfico QxP
plt.plot(x, y, 'o', label='dados')
plt.plot(x, yfitted, '-', label='curva de ajuste ')
plt.xlabel('tempo(min)')
plt.ylabel('Pressão(mbar)')
plt.legend()
plt.savefig('Pxt.png')
plt.show()
