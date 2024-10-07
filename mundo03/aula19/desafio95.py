dados_jogador = dict()
lista_jogadores = list()

while True:
    dados_jogador['nome'] = str(input('Nome do Jogador: '))
    qts_partidas_disputadas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou ?: '))

    lista_de_gols = list()  # Reinicializa a lista de gols para cada jogador
    total_gols = 0  # Reinicializa o total de gols para cada jogador

    for contador in range(0, qts_partidas_disputadas):
        gols_por_partida = int(input(f'Quantos gols na partida {contador}?: '))
        total_gols += gols_por_partida
        lista_de_gols.append(gols_por_partida)

    dados_jogador['gols'] = lista_de_gols
    dados_jogador['total'] = total_gols

    lista_jogadores.append(dados_jogador.copy())

    resposta = str(input('Quer continuar [S/N]? : ')).strip().upper()
    if resposta == 'N':
        break

print(f'{"Cod":<4}{"NOME":<10}{"Gols":>8}{"total":>10}')
for indice, valor in enumerate(lista_jogadores):
    print(f'{indice:<4}{valor["nome"]:<10}{str(valor["gols"]):>8}{valor["total"]:>10}')

while True:
    jogador_escolhido = int(input('Mostrar dados de qual jogador? (coloque o cod: (999) para interromper) : '))
    if jogador_escolhido == 999:
        break
    if jogador_escolhido < len(lista_jogadores):
        jogador = lista_jogadores[jogador_escolhido]#   # jogador recebe o bloco escolhido da lista de jogadores
        print(f'Levantamento do jogador {jogador["nome"]}')
        for indice, gols in enumerate(jogador['gols']):
            print(f'Na partida {indice} fez {gols} gols')
    else:
        print("Código inválido. Tente novamente.")
