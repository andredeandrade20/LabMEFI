import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

## Carregamento da base de dados
def loadData():
    chunks = []
    for chunk in pd.read_csv('C:/Users/Ygoor/Desktop/Facul/LABS/dados_c.csv', encoding = 'UTF-8', sep = ',', low_memory = True, chunksize=1000):
        chunks.append(chunk)
    df = pd.concat(chunks)
    df = df.astype(float)
    return df

df = loadData()
x = df['tempo (s)']*(1/60)
y = df['ln(P/P0)']

## Cálculo de S

tm = x.mean()
P = y.mean()
Po = df.iloc[0,1]
V = 11.9103
PPo = ((P/Po)*(-1))
ln = (np.log(PPo))*(-1)
S = ((ln*V)/tm)
print('O valor de S:', S)

## Gráfico ln(P/P0) x t
plt.plot(x, y, 'o', label='dados')
plt.xlabel('tempo(s)')
plt.ylabel('ln(P/P0)')
plt.legend()
plt.savefig('lnxt.png')
plt.show()
