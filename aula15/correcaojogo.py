import random
import time
print('=-'*15)
print('vamos jogar par ou impar ? :')
print('=-'*15)
time.sleep(1)

vitorias = 0
derrotas = 0

while True :
    numero_computador = random.randint(1,10)
    numero_jogador = int(input('diga um valor : '))
    escolha_par_impar = str(input('Par ou Impar? [P / I] :')).strip().upper()
    soma_escolhas = numero_computador + numero_jogador
    print(f'voce jogou {numero_jogador} e o computador jogou {numero_computador}')
    
    if soma_escolhas % 2 == 0:
        resultado = 'Par'
    else:
        resultado = 'Impar'
        
    if escolha_par_impar == 'P' and resultado == 'Par' or escolha_par_impar =='I' and resultado == 'Impar':
        print(f'voce escolheu o numero {numero_jogador} e o computador escolheu {numero_computador}')
        print(f'somando os dois fica {soma_escolhas}, o resultado é {resultado}')
        print('voce ganhou !')
        vitorias +=1
    else:
        print(f'game over ,voce perdeu mas venceu {vitorias} vezes',)
        break
        

    