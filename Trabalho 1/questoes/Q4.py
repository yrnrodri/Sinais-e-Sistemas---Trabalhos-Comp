# 4)
# Duas funções importantes para o estudo de sinais é a função impulso unitário
# e a função degrau unitário. E possível chegar de uma função na outra como visto em aula. 
# Implemente a função degrau a partir da função impulso (soma acumulativa), e função impulso
# a partir da função degrau (primeira diferença). Além disso, faça uma onda quadrada a partir
# da função degrau que foi implementada. Plote os gráficos.

import matplotlib.pyplot as plt
import numpy as np

# função degrau unitário
n = np.arange(-5, 6)

def impulso_unitario_comum(m):
    return np.where(m == 0, 1, 0)
       
def degrau_unitario(n):
    degrau = []
    i_n2 = impulso_unitario_comum(n)
    valor = 0
    for i in range(len(n)):
        valor = valor + i_n2[i]
        degrau.append(valor)
    
    return np.array(degrau)
    
             
u_n = degrau_unitario(n)

# função impulso unitário

def degrau_unitario_comum(n):
    return np.where(n >= 0, 1, 0)

def impulso_unitario(m):
    impulso = []
    u_n2 = degrau_unitario_comum(m)
    
    for i in range(len(m)):
        if i == 0:
            valor = u_n2[i]
        else:
            valor = u_n2[i] - u_n2[i - 1]
        
        impulso.append(valor)
 
    return np.array(impulso)

i_n = impulso_unitario(n)

# onda quadrada

def onda_quadrada(n, periodo):
    return degrau_unitario(n % periodo) - degrau_unitario((n % periodo) - periodo // 2)

quadrado_n = onda_quadrada(n, 4)


# gráficos

plt.subplot(3, 1, 1)
plt.stem(n, u_n, basefmt=" ")
plt.title('Função degrau')
plt.xlabel('n')
plt.ylabel('u[n]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, i_n, basefmt=" ")
plt.title('Função impulso')
plt.xlabel('n')
plt.ylabel('δ[n]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, quadrado_n, basefmt=" ")
plt.title('Onda Quadrada')
plt.xlabel('n')
plt.ylabel('Square Wave')
plt.grid(True)

plt.tight_layout()
plt.show()