# Considereando x[n] um sinal contendo as N amostras (n = {0, 1, ..., N − 1})
# ruidosas de um sinal x(t) = f(t)u(t), onde

# f(t) = 0.75e ^(−0.275t ) * ( 4 cos (4t + (π / 3) ) +  5 sin(t) )  , t ∈ [0, 10]s

# presentes no arquivo (samples.csv) disponibilizado no SIGAA, obtenha y[n] para os sistemas
# representados pelas seguintes relações de entrada e saída:

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv("Trabalho 1\material\samples.csv")
x_n = dados['x_n'].values
t_n = dados['t_n'].values
n = np.arange(0, len(t_n))


# a) y[n] = y[n − 1] + x[n], respeitando a condição inicial y[−1] = 0.

y_n = [x_n[0]] # y[0] = y[-1] + x[0] -> y[0] = x[0]

for i in range(1, len(t_n)):
    y = y_n[i - 1] + x_n[i]
    y_n.append(y)
    
# b) y[n] = (1 / 2M + 1) Σ de k = -M a M (x[n - k])], onde M < N ∈ N é o parâmetro que deve ser ajustado de modo
# a “eliminar” o ruído presente no sinal.

M = 50

def somatorio(M, j):
     soma = 0
     for k in range(-M, j + 1):
         dif = j - k
         if dif < len(x_n):
            soma += x_n[dif]
        
     return soma

constante = 1 / (2 * M + 1)
soma_0 = somatorio(M, 0)
y_n2 = [constante * soma_0]
       
for w in range(1, len(t_n)):
    soma_n = somatorio(M, w)
    y2 = constante * soma_n
    y_n2.append(y2)

# A)
plt.subplot(2, 2, 1)
plt.stem(n, x_n, basefmt=" ")
plt.title('Função x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.stem(n, y_n, basefmt=" ")
plt.title('Função y[n]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)

# B)

plt.subplot(2, 2, 3)
plt.stem(n, y_n2, basefmt=" ")
plt.title('Função y2[n]')
plt.xlabel('n')
plt.ylabel('y2[n]')
plt.grid(True)

plt.tight_layout()
plt.show()