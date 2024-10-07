import random
import math

contador = 0
numeros_sorteados = []
while contador < 5:
    numeros = random.randint(1,10)
    numeros_sorteados.append(numeros)#aqui vai armazenar e por ao lado 1,2,3 ate o contador terminar
    contador +=1
print(f'os numeros sorteados foram {numeros_sorteados}')    
print(f'o maior valor foi {max(numeros_sorteados)} e o menor valor foi {min(numeros_sorteados)}')
