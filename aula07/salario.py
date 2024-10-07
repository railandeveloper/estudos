salario_atual = float(input('Qual é o salario do funcionario? R$'))
porcentagem = salario_atual * 15/100  # para calcular quanto é 15 % do salario
salario_com_aumento = salario_atual + porcentagem
print(
    f'um funcionario que ganhava R${salario_atual}, com 15% de aumento passa a receber R$ {salario_com_aumento:.2f}')
