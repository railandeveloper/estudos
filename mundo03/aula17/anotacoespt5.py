# para criar uma lista vazia, duas formas
# valores = []
# valores = list()

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

#pegue o indice e o valor da lista valores
for indice, valor in enumerate(valores):  # o enumerate pega o indice e o valor 
    print(f'na posicao {indice} esta o valor {valor}...')
print('cheguei ao final da lista')    
