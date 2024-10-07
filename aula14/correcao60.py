import time
import math

numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
print(f'calculando fatorial de {numero} !')
fatorial = math.factorial(numero)
while contador > 0:
    print(f'{contador} ', end=' ')  # o end é usado para n pular linhas
    print(' x ' if contador > 1 else ' = ', end ='') #se o contador for maios que 1 ira exibir x, se nao exibira o =
    contador -= 1
print(f'{fatorial}')
