'''elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condicao de pagamento:
a vista 10% desconto
a vista cartao 5%
em ate 2x no cartao, preco normal
3x ou mais no cartao,20%juros'''

formaPagamento = input('Qual a forma de pagamento? (a vista / a vista no cartao / 2x no cartao / 3x ou mais no cartao): ')

valorProduto = 50
calculoDinheiroAvista = valorProduto *10/100#calculo de 10%
CalculoAvistaCartao = valorProduto * 5/100
CalculoJuros = valorProduto *20/100

if formaPagamento == 'a vista':
    print(f'Com 10% de desconto, o produto custará: R${valorProduto-calculoDinheiroAvista:.2f}')
elif formaPagamento == 'a vista no cartao':
    print(f'Com 5% de desconto no cartão, o produto custará: R${valorProduto - CalculoAvistaCartao}')
elif formaPagamento == '2x no cartao':
    print('preco normal')
elif formaPagamento == '3x ou mais no cartao':
    print(f'Com 20% de juros para 3x ou mais no cartão, o produto custará: R${valorProduto +CalculoJuros}')
else:
    print('forma de pagamento invalida')

