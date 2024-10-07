import random
numeros = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))#colancando dentro dos parenteses vira uma tupla, e ja e sorteado os 5 numeros aleatorios
print(f'voce sorteou os valores : {numeros}')
for numero in numeros:
    print(f'{numero}', end =' ')
   
print(f'o maior valor foi {max(numeros)} e o menor valor foi {min(numeros)}')
   
