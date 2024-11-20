# 1)
# Considere um sinal senoidal no tempo discreto e que P
# seja a quantidade de amostras do sinal por período. Plote um único período da senoide com
# frequência de 60Hz e com P = {3, 5, 10, 50} amostras.

import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
frequencia = 60 
T = 1 / frequencia  
P_vals = [3, 5, 10, 50]  

# Criação da figura para os subplots
plt.figure(figsize=(10, 8))

# Gerando e plotando a senoide para cada valor de P
for i, P in enumerate(P_vals, 1):
    t_discreto = np.linspace(0, T, P, endpoint=False)
    x_discreto = np.sin(2 * np.pi * frequencia * t_discreto)
    
    # Subplot para cada valor de P
    plt.subplot(2, 2, i)
    plt.stem(t_discreto, x_discreto, basefmt=" ")
    plt.plot(t_discreto, x_discreto, 'o', color='red')
    plt.title(f'Amostras por Período: P = {P}')
    plt.xlabel('Tempo (n)')
    plt.ylabel('Amplitude')
    plt.grid(True)


plt.tight_layout()
plt.show()
