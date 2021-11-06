from itertools import permutations #>>>> BIBIOTECA PARA PERMUTAR
import time #BIBLIOTECA PARA CALCULAR TEMPO
inicio = time.time() 

####### CALCULAR PERMUTAÇÕES #######
def permute(data, i, length): 
    if i==length: 
        print(''.join(data))
    else:
      for j in range(i,length): 
        #swap
        data[i], data[j] = data[j], data[i] 
        permute(data, i+1, length) 
        data[i], data[j] = data[j], data[i]

####### DEFININDO VARIÁVEIS #######
string = "ABDCD" #>>>> STRING PARA PERMUTAR
n = len(string) 
data = list(string)     
permute(data, 0, n)

####### MOSTRAR TEMPO DE EXECUÇÃO #######
fim = time.time()
diferenca = fim - inicio
print(f'\nO tempo de execução foi de: {diferenca} seg.')