
valores = list()
for contador in range(0,5):
    valores.append(int(input('digite um numero : ')))#todos os numeros inseridos pelo usuario ficarao salvos na lista valores


# pegue o indice e o valor da lista valores
for indice, valor in enumerate(valores):  # o enumerate pega o indice e o valor
    print(f'na posicao {indice} esta o valor {valor}...')
print('cheguei ao final da lista')
