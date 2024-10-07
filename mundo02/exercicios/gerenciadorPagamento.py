'''elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condicao de pagamento:
a vista 10% desconto
a vista cartao 5%
em ate 2x no cartao, preco normal
3x ou mais no cartao,20%juros'''

print('=' * 40)
print('{:^40}'.format('lojas railan'))
print('=' * 40)




precoCompras = float(input('preço das compras : R$ '))
print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque: 10% de desconto')
print('[2] à vista no cartão: 5% de desconto')
print('[3] em até 2x no cartão: preço formal')
print('[4] 3x ou mais no cartão: 20% de juros')

opcaoPagamento = int(input('digiteo o numero da sua opcao de pagamento :'))

descontoAvista = precoCompras *10/100
descontoAvistaCartao = precoCompras *5/100
duasVezesCartao = precoCompras/2
parceladoVariasVezes = precoCompras *20/100

if opcaoPagamento ==1:
    print(f'sua compra de R${precoCompras} vai custar R${precoCompras - descontoAvista} com os 10% de desconto ')
elif opcaoPagamento == 2:
    print(f'sua compra de R${precoCompras} vai custar R${precoCompras-descontoAvistaCartao} com os 5% de desconto')
elif opcaoPagamento == 3:
    print(f'preco normal sem desconto pagando em duas vezes de R${duasVezesCartao}')
else:
    print(f'sendo parcelado em 3 vezes ou mais custara R${precoCompras + parceladoVariasVezes}')