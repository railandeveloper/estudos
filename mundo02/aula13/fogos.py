'''Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''



import time

print('=' * 40)
print('{:^40}'.format('contagem regressiva!!!'))
print('=' * 40)


#Esse código em Python está usando um loop "for" para iterar sobre uma sequência de números começando em 10 e indo até 1 (excluindo o 0), com passos de -1. Isso significa que ele vai começar em 10, depois ir para 9, 8, 7, e assim por diante até 1.

for comando in range(10, 0, -1):
    print(comando)
    time.sleep(1)
print('{:^40}'.format('FELIZ ANO NOVO !!!'))