import matplotlib.pyplot as plt #>>>BIBLIOTECA PARA UTILIZAR OS GRÁFICOS                  
import math #>>>BIBLIOTECA PARA CALCULAR LOG

####### VARIÁVEIS #######
fig, ax = plt.subplots(figsize = (9, 6))
fsize = 22
xlab = 'Conjunto de dados'                      
ylab = 'Instruções'

####### ESTRUTURA PARA INSERIR AS FUNÇÕES #######
i = list(range(1, 101))                              
resultado_1 = [math.pow(2, n) for n in i]
#resultado_2 = [n * math.log(n, 2) for n in i]
#resultado_3 = [n for n in i]

####### PLOTAR FUNÇÕES NO GRÁFICO #######
plt.plot(resultado_1)                    
#plt.plot(resultado_2) 
#plt.plot(resultado_3) 

####### CONFIGURAR GRÁFICO #######
ax.set_xlabel(xlab, fontsize = fsize) 
ax.set_ylabel(ylab, fontsize = fsize) 
ax.tick_params(labelsize = 15) 
ax.grid(ls = '--')  

####### SALVAR FIGURA #######
fig.savefig('3^n.png')

####### MOSTRAR GRÁFICO #######
plt.show()