from itertools import permutations ### BIBLIOTECA PARA PERMUTAÇÃO
import time ### BIBLIOTECA PARA TEMPO DE EXECUÇÃO

inicio = time.time() #>>> iniciar contagem do tempo

def permute(data, i, length): #>>> laço que realiza a permutação
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            #swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]

string = "ABCDE" #>>> string para permutar
n = len(string)
data = list(string)
permute(data, 0, n)

fim = time.time() #>>> finalizar contagem do tempo
diferenca = fim - inicio
print(f"\nO tempo de execução foi de: {diferenca} seg.\n") 