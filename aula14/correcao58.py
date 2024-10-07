''': Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''

import random
numero_computador = random.randint(1,10)
palpite = 0
tentativas = 0

print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar ?')

while palpite != numero_computador:
    palpite = int(input('digite o seu palpite : '))
    tentativas +=1
    if palpite == numero_computador:
        print(f'o numero secreto é {numero_computador}')
        print('parabens por acertar')
        print(f'voce precisou de {tentativas} tentativas ')
    elif palpite > numero_computador:
        print('o numero e menor')
    else:
        print('o numero e maior')
print('fim do programa')        
        