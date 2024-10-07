#faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#exemplo : 1834
# unidade 4
# dezena 3
# centena 8
# milhar 1

#manupulando texto
numero =(input('digite um numero :'))
print(f'unidade :{numero[3]}')
print(f'dezena :{numero[2]} ')
print(f'centena :{numero[1]}')
print(f'milhar :{numero[0]}')

#de forma matematica
num = int(input('Informe um numero: '))
print(f'Analisando o numero {num}')
unidade = num //1