import random
import time

valores = list()

print('-'*20)
print(f'JOGO DA MEGA SENA')
print('-'*20)
quantidade_de_jogos = int(input('quantos jogos voce quer que eu sorteie ? : '))
print(f'sorteando {quantidade_de_jogos} jogos ...')
time.sleep(2)

for contador in range(1, quantidade_de_jogos+1):
    numeros_sorteados = random.sample(range(1, 61), 6)
    print(f'jogo {contador}: {numeros_sorteados}')
    time.sleep(1)
    
print("-="*15 + " < boa sorte > " + "-="*15)

  
    