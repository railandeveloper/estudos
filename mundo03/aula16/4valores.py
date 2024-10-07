numeros_sorteados = []
for contador in range(1,5):
    valores = int(input(f'digite o {contador} numero :'))
    numeros_sorteados.append(valores)#coleta os numeros e salva em uma lista
print(f'os numeros digitados foram {numeros_sorteados}')
posicao_numero = numeros_sorteados.index(3)
print(f'o valor 9 apareceu {numeros_sorteados.count(9)} vezes')
print(f'o numero 9 apareceu na posicao {posicao_numero}')
