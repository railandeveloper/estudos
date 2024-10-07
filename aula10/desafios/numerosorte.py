'''escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir, o programa devera escrever na tela se o usuario venceu ou perdeu'''

import random
from time import sleep# para fazer o computador dormir pelo tempo que voce informar
numeroDaSorte = random.randint(0,10)
numeroDigitado = int(input('digite o numero da sorte :'))

print('Processando...')
sleep(3)#o computador domira por 2 seg
if numeroDaSorte == numeroDigitado:
    print('voce venceu')
else:
    print('voce perdeu')
