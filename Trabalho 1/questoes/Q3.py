# 3)
# Mostre graficamente que o aumento da frequência ω0 em um sinal exponencial
# complexo periódico x[n] = e^jω0n não necessariamente aumenta a oscilação. Explique o motivo.
# Além disso, qual a frequência que faz o sinal oscilar mais rápido?

import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 15)
frequencias = [0.2 * np.pi, 0.5 * np.pi, np.pi, 1.5 * np.pi]

for i, omega in enumerate(frequencias, 1):
    x_n = np.exp(1j * omega * n)
    
    plt.subplot(2, 2, i)
    plt.stem(n, np.real(x_n), basefmt=" ")
    plt.title(f'Frequência Angular ω = {omega / np.pi:.1f}π rad')
    plt.xlabel('n')
    plt.ylabel('Re{x[n]}')
    plt.grid(True)

plt.tight_layout()
plt.show()

# Considerando um W = Wo + 2pi, teríamos: e^(j2pin) * e^(jWon), que é o mesmo que somente e^(jWon)
# indicando assim uma periodicidade, não importa o quanto aumente o Wo, ele chegará a um ponto
# máximo, e depois reiniciará, sendo assim, de 0 a pi, onde o sinal oscila mais rápido em 
# Wo = pi