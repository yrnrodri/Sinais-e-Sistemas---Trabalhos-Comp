# Considerando x[n] um sinal contendo as N amostras (n = {0, 1, ..., N − 1})
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

y_n2 = np.zeros(len(t_n))

def filtragem(i, M):
    constante = 1 / (2 * M + 1)
    soma = 0
    for k in range(-M, M + 1):
        if (i - k) >= 0 and (i - k) < len(t_n):
            soma += x_n[i - k]
    return constante * soma

for j in range(0, len(t_n)):
    y_n2[j] = filtragem(j, 11)

        
# Descobrindo o melhor M

erro_quadratico = np.zeros(70)

T = np.linspace(0, 10, 1000)

def f(t):
    return 0.75 * np.exp(-0.275 * t) * (4 * np.cos(4 * t + (np.pi / 3)) + 5 * np.sin(t))

f_t = f(T)

m = np.arange(0, 70)

for M_i in m:
    Y = np.zeros(len(t_n))
    for indice in range(0, len(t_n)):
        Y[indice] = filtragem(indice, M_i)
      
    erro = np.mean((f_t - Y) ** 2)
    erro_quadratico[M_i] = erro
    
indice_minimo = np.argmin(erro_quadratico)
print(indice_minimo) # Esse vai ser o melhor M


# A)
plt.subplot(2, 2, 1)
plt.plot(n, x_n)
plt.title('Função x[n]')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(n, y_n)
plt.title('Função y[n]')
plt.xlabel('n')
plt.ylabel('y[n]')
plt.grid(True)

# B)

plt.subplot(2, 2, 3)
plt.plot(n, x_n, label='x[n]')
plt.plot(n, y_n2, color='red', label='y[n]')
plt.title('Função y2[n]')
plt.xlabel('n')
plt.ylabel('y2[n]')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(m, erro_quadratico, label='Erro quadratico')
plt.title('Erro quadratico')
plt.xlabel('M')
plt.ylabel('EQM')
plt.grid(True)

plt.tight_layout()
plt.show()