def ficha(nome ='desconhecido', gols =0): 
    print(f'o jogador {nome} fez {gols} gol(s) no campeonato')


print('-'*25)
nome_jogador = str(input('Nome do jogador: '))
numero_gols = str(input('Numero de gols?: '))
if numero_gols.isnumeric():
    numero_gols = int(numero_gols)
else:
    numero_gols = 0
if nome_jogador.strip() == '':#se o nome do jogador for igual a vazio, n for digitado
   ficha(gols= numero_gols)#vai imprimir apenas os gols, e o parametro desconhecido
else:
    ficha(nome_jogador, numero_gols) #se for passado nome, ele passa nomee e gols    
   