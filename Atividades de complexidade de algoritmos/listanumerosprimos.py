import matplotlib.pyplot as plt
import math
import time

fig, ax = plt.subplots(figsize=(9, 6))
fsize = 22
xlab = 'N'
ylab = 'Tempo'

N = int(input("Insira o valor de N: "))
cont = N
N = 1

while N < cont:
    inicio = time.time()
    A = list(range(2, N))
    for i in range(2, int(math.sqrt(N) + 1)):
        if i in A:
            for j in range(i**2, N, i):
                if j in A: A.remove(j)

    print(f'Os números primos antecedidos de {N} são >>>', A)
    N += 1
    fim = time.time()
    diferenca = fim - inicio
    plt.plot(N, diferenca, 'o')
    print(f'Tempo de execução: {diferenca} seg.')
    print('---------------------------------------------')

ax.set_xlabel(xlab, fontsize=fsize)
ax.set_ylabel(ylab, fontsize=fsize)
ax.tick_params(labelsize=15)
ax.grid(ls='--')
plt.show()
