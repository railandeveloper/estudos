import random
import time

print('=' * 40)
print('{:^40}'.format('Bem vindo ao JOKENPO !!!'))
print('=' * 40)

itens = ('pedra', 'papel', 'tesoura',)

# joada comptudaro recebe um numero de 0 a 2
jogadaComputador = random.randint(0, 2)

# print(f'o computador escolheu {itens[jogadaComputador]}')# ao inves de escrever entre um numero de 0 a 2, ele vai escrever 'pedra papel ou tesoura, pegando do indice da variavel itens. se le assim : o computador escolheu o item pedra, papel,tesoura.o ramdom embaralha

print('''Suas opcoes:
   [ 0 ] PEDRA
   [ 1 ] PAPEL
   [ 2 ] TESOURA''')

suaJogada = int(input('Qual é a sua joagada?:'))
print('JO')
time.sleep(2)
print('KEN')
time.sleep(2)
print('PO!!!')
time.sleep(1)

print(f'o computador escolheu {itens[jogadaComputador]}')
# jogador escolheu o item do indice digitado pelo jogador
print(f'voce escolheu {itens[suaJogada]}')

if suaJogada == 0 and jogadaComputador == 2 or suaJogada == 1 and jogadaComputador == 0 or suaJogada == 2 and jogadaComputador == 1:
    print('voce venceu')
elif suaJogada == jogadaComputador:
    print('empate, jogue novamente para tentar vencer')
else:
    print('voce perdeu')
