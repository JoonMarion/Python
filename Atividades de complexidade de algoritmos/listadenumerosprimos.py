import matplotlib.pyplot as plt
import time
inicio = time.time() 

### CONFIGURAÇÕES DO GRÁFICO ###
fig, ax = plt.subplots(figsize = (9, 6))
fsize = 22
xlab = 'n'                      
ylab = 'Tempo'

### LISTANDO NÚMEROS PRIMOS ###
n = 2000 # >>>> INSERIR NÚMERO 
A = []
x = 1
for i in range(2, n):
  j = 2
  while j < i and i % j != 0:
    j += 1
    if (j == i):
      A.append(i)
      x += 1
print(A)

### FINALIZANDO CONTAGEM DE TEMPO / PLOTANDO E PRINTANDO RESULTADO ###
fim = time.time()
diferenca = fim - inicio
plt.plot(n, diferenca, 'o')
print(f'\nTempo de execução: {diferenca} seg.\n')

### CONFIGURAÇÕES DO GRÁFICO E PRINTANDO GRÁFICO###
ax.set_xlabel(xlab, fontsize = fsize) 
ax.set_ylabel(ylab, fontsize = fsize) 
ax.tick_params(labelsize = 15) 
ax.grid(ls = '--')  
plt.show()