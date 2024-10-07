#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.


numero = float(input('digite um valor '))
print(f'voce digitou {numero}, sendo sua parte inteira {numero:.0f}')

#utilizando modulos
import math
num = float(input('digite um valor '))
print(f'voce digitou {num}, sendo sua parte inteira {num.__trunc__()}')
#o metodo trunc retorna a parte inteira do numero
