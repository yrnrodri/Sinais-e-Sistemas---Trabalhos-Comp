# 2)
# Seja x[n] um sinal exponencial complexo de tempo discreto dado por x[n] = Ce^(an)
# A partir desta expressão, defina as constantes a, C de modo a obter:


import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 15)

# A) O sinal exponencial
# Escolhendo C = 1 e a = 1 pois nesse caso, o numero de euler
# já basta para o sinal ser exponencial

C = 1
a_1 = 1

x_A = C * np.exp(a_1 * n)

# B) O sinal exponencial complexo oscilatório.
# Escolhendo C = 1 e a = j * 2 * pi * f, pois assim a exponencial será complexa
# e pela formula de euler, também será oscilatória 

omega = 2 * np.pi * 50
a_2 = 1j * omega

x_B = C * np.exp(a_2 * n)

plt.figure(figsize=(12, 8))

# C) O sinal exponencial complexo oscilatório amortecido.
# Para esse sinal, temos a equação: x[n] = |C|e^(jθ) * |α|^n * e^(jWn)
# que também pode ser reescrita como: x[n] = |C||α|^n(cos(Wn + θ) + jsen(Wn + θ))
# com um comportamento crescente se |α| > 1, e decrescente para |α| < 1
# nesse , em vez de escolher um a, escolherei um α para manipular o sinal
# onde α = |α|e^(jW) e x[n] = Cα^n

teta = np.pi
alpha = 0.6
x_C = C * np.power(alpha, n) * np.cos(omega * n + teta) + 1j * C * np.power(alpha, n) * np.sin(omega * n + teta)

# letra A
plt.subplot(3, 2, 1)
plt.stem(n, x_A, basefmt=" ", label=f'Exponencial: a={a_1}')
plt.title('Sinal Exponencial')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.grid(True)

# letra B

plt.subplot(3, 2, 2)
plt.stem(n, np.imag(x_B), basefmt=" ", label=f'Exponencial: a={a_2}')
plt.title('Sinal Exponencial Complexo Oscilatório')
plt.xlabel('n')
plt.ylabel('Im{x[n]}')
plt.grid(True)

# letra C

plt.subplot(3, 2, 3)
plt.stem(n, np.imag(x_C), basefmt=" ", label=f'Exponencial: a={alpha}')
plt.title('Sinal Exponencial Complexo Oscilatório Amortecido')
plt.xlabel('n')
plt.ylabel('Im{x[n]}')
plt.grid(True)

plt.tight_layout()
plt.show()

