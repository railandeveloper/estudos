cotacaoEuro = 5.39
valorEmReais = float(input('quanto voce tem em dinheiro na carteira?R$'))
valorConvertido = valorEmReais / cotacaoEuro
print(f'com R${valorEmReais} reais voce pode comprar €{valorConvertido:.2f} euros')