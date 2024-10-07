'''escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar

calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado'''

valorCasa = float(input('Qual o valor da casa? : '))
salarioComprador = float(input('Qual o salário do comprador? : '))
qtdAnosParaPagamento = int(input('Em quantos anos pretende pagar? : '))
calculoPorcentagem = salarioComprador * 30 / 100  # calculando 30% do salário
mensalidade = valorCasa / (qtdAnosParaPagamento * 12)  # convertendo anos para meses
print(f'R${calculoPorcentagem:.2f} equivale a 30% do seu salário.')
print(f'O valor da mensalidade será R${mensalidade:.2f} reais.')

if mensalidade > calculoPorcentagem:
    print('Portanto, o empréstimo não foi aprovado.')
else:
    print('Portanto, o empréstimo foi aprovado.')

