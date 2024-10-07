'''faça um programa que pergunte o salario do funcionario e calcule o valor do seu aumento
para salarios superiores a 1250 reais calcule um  aumento de 10%
para inferiores ouy iguais, o aumento é de 15%'''

salario = float(input('digite o seu salario em reais :$ '))

if salario > 1250:
    aumento = salario *10 / 100#vai calcular 10% do valor digitado
    print(f'voce esta recebendo ${salario} reias, com o aumento de 10% voce passa a receber ${salario+aumento} reais')
else:
    aumento = salario *15/100
    print(f'voce recebe ${salario} reais, com o aumento de 15% voce passa a receber ${salario+aumento} reais')
    
    '''salario = float(input('Digite o seu salário em reais: '))

# Calcula o aumento com base na condição
if salario > 1250:
    percentual_aumento = 10
else:
    percentual_aumento = 15

# Calcula o valor do aumento
aumento = salario * percentual_aumento / 100

# Exibe a mensagem com o salário original e o novo salário após o aumento
print(f'Você recebe R${salario:.2f}. Com o aumento de {percentual_aumento}%, passará a receber R${salario + aumento:.2f}.')
Neste código, a principal melhoria é calcular o aumento uma única vez, com base na condição, e, em seguida, utilizá-lo para exibir a mensagem, eliminando a duplicação de código. Isso torna o código mais limpo, mais fácil de manter e menos propenso a erros se a lógica precisar ser alterada no futuro.'''