import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## Carregamento da base de dados
def loadData():
    chunks = []
    for chunk in pd.read_csv('C:/Users/Ygoor/Desktop/Facul/LABS/dados_a.csv', encoding = 'UTF-8', sep = ',', low_memory = True, chunksize=1000):
        chunks.append(chunk)
    df = pd.concat(chunks)
    df = df.astype(float)
    return df

## Definição dos eixos, cálculo de S e conversão de unidades
df = loadData()
df['S (ml/min)'] = df['Q (mbar.cc/min) (mbar.mL/min)']/df['pressao (mbar)']
ys = df['S (ml/min)']*(0.001*(1/3600))
yq = df['Q (mbar.cc/min) (mbar.mL/min)']*(0.001*(1/3600))
x = df['pressao (mbar)']

## Função de otimização para curva exponencial em Q
def qfunc(x,p1,p2):
    return p1*x + p2

## Otimização QxP
poptq, pcovq = curve_fit(qfunc, x, yq, p0 = (1, 0))
pq1, pq2 = poptq
yqfitted = qfunc(x, *poptq)

## Cálculo de parâmetros para QxP
mediaq = yq.mean()
dpq = yq.std()
varq = yq.var()
corrq = yq.corr(x)
print(pq1,'.x + ',pq2)
print('Média: ', mediaq)
print('Desvio padrão: ', dpq)
print('Variância: ', varq)
print('Corr: ', corrq)

## Gráfico QxP
plt.plot(x, yq, 'o', label='dados')
plt.plot(x, yqfitted,'-', label='curva de ajuste ')
plt.xlabel('Pressão(mbar)')
plt.ylabel('Fluxo(mbar.cm3/h)')
plt.title('QxP')
plt.legend()
plt.savefig('QxP.png')
plt.show()

## Função para S
def sfunc(x,s1,s2):
    return s2 + s1*(np.exp(-x))

## Otimização SxP
popts, pcovs = curve_fit(sfunc, x, ys, p0 = (1, 0))
ps1, ps2 = popts
ysfitted = sfunc(x, *popts)

## Cálculo de parâmetros para SxP
medias = ys.mean()
dps = ys.std()
vars = ys.var()
corrs = ys.corr(x)
print('')
print(ps2,'+',ps1,'e^(-x)')
print('Média: ', medias)
print('Desvio padrão: ', dps)
print('Variância: ', vars)
print('Corr: ', corrs)

## Gráfico SxP
plt.plot(x, ys, 'o', label='dados')
plt.plot(x, ysfitted, '-', label='curva de ajuste ')
plt.xlabel('Pressão(mbar)')
plt.ylabel('Velocidade de saída(cm3/h)')
plt.title('SxP')
plt.legend()
plt.savefig('SxP.png')
plt.show()
