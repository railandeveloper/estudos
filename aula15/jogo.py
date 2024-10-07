import random
import time

vitorias = 0
derrotas = 0

print('vamos jogar Par ou impar ? ')
time.sleep(0.1)
while True:
    numero_computador = random.randint(1,10)
    numero_jogador = int(input('Digite um valor ? : '))
    escolha_jogador = str(input('Par ou Impar ? [P/I] : ')).strip().upper()
    soma_escolhas = numero_jogador + numero_computador
    
    if soma_escolhas %2 == 0:
       resultado = 'Par'
    else:
        resultado = 'Impar'

    print(f'voce jogou {numero_jogador} e o computador jogou {numero_computador}. total de {soma_escolhas}, Deu {resultado}')
 
    
    if escolha_jogador == 'P' and resultado == 'Par' or escolha_jogador == 'I' and resultado == 'Impar':
        vitorias +=1
        print('voce ganhou')

    else:
        derrotas+=1
        print('voce perdeu')
        
    jogar_novamente = str(input('voce quer continuar jogando ? [S / N] ?')).strip().upper()
    if jogar_novamente != 'S':
        break

print(f'voce teve um total de {vitorias} vitorias e {derrotas} derrotas')
           
        
         
     # se escolha jogador for diferente da soma da escolhas,voce perdeu    
         
         
        
    
    
   
    

      
   
        

