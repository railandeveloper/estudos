'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random
import time
from _operator import itemgetter

resultados_jogos = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6),
}
ranking = list()

for chave, valor in resultados_jogos.items():
    print(f'o {chave} tirou {valor}')
    time.sleep(1)

#vamos ordenar o ranking pela chave valor 1, que seria o resultado, se fosse valor 0 seria a chave 'jogador'   
ranking = sorted(resultados_jogos.items(), key=itemgetter(1), reverse=True)#O Reverse true coloca em ordem decrescente, do maior para o 
#coloque em ordem decrescente o valor de resultado de jogos e jogue na lista ranking

for indice, valor in enumerate(ranking):
    print(f'{indice+1} lugar {valor[0]} com {valor[1]}')

    
    
    
    
    
