import random
numeros = list()

def sorteio():
    numeros_sorteados =random.sample(range(1, 101), 5)
    numeros.extend(numeros_sorteados)
    print(f'os numeros sorteados são {numeros}')
    print('-='*20)
    
def somapar():
   soma = 0
   contador_par = 0
   for numero in numeros:
       if numero % 2 == 0:
           soma += numero 
           contador_par +=1          
   print(f'sao {contador_par} numeros pares, e a soma deles é {soma}') 

sorteio()
somapar()

        