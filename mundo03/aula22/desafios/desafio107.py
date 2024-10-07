import moeda

#programa principal
valor = float(input(f'Digite o preço: R$: '))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'o dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor)}')