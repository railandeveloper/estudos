''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. '''

valores = list()
for contador in range(0,5):
    valores.append(int(input(f'digite um valor para a posicao {contador}  : ')))


# pegue o indice e o valor da lista valores
for indice, valor in enumerate(valores):  # o enumerate pega o indice e o valor 
    print(f'na posicao {indice} esta o valor {valor}')
print(f'o maior valor foi {max(valores)} e o menor foi {min(valores)}') 

'''valores = list()
for contador in range(1, 6):
    valores.append(int(input(f'digite o {contador}º valor: ')))

print(f'Você digitou os valores: {valores}')

                                            #para pegar a posicao do maior valor
print(f'O maior valor é {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor é {min(valores)} na posição {valores.index(min(valores))}')
'''  