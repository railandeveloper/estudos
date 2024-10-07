dados_jogador = dict()
lista_de_gols = list()
total_gols = 0

dados_jogador['nome'] = str(input('Nome do Jogador: '))
qts_partidas_disputadas = int(input(f'quantas partidas {dados_jogador["nome"]} jogou ?: '))

for contador in range(0,qts_partidas_disputadas):
    gols_por_partida = int(input(f'quantos gols na partida {contador}?: '))
    total_gols = total_gols+gols_por_partida
    lista_de_gols.append(gols_por_partida)

dados_jogador['gols'] = lista_de_gols
dados_jogador['total'] = total_gols
print('-='*20)
print(dados_jogador)  
print('-='*20)  

for chave, valor in dados_jogador.items():
    print(f'o campo {chave} tem o valor {valor}')
print('-='*20)
print(f'o jogador {dados_jogador["nome"]} jogou {qts_partidas_disputadas} partidas')


for indice, valor in enumerate(lista_de_gols):
    print(f' => na partida {indice}, fez {valor} gols')  
print(f'foi um total de {total_gols} gols')    
