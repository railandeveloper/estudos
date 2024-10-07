'''Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

import math

# Solicita o número ao usuário
numero = int(input('Digite um número para calcular seu fatorial: '))

# Calcula o fatorial usando a função math.factorial()
fatorial = math.factorial(numero)

# Exibe o resultado
print(f'O fatorial de {numero} é {fatorial}')
