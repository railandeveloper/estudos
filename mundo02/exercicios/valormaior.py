'''Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela a mensagem:
o primeiro valor é maior
o segundo valor é maior
nao existe valor maior, os dois sao iguais'''

num1 = int(input('digite o pimeiro numero : '))
num2 = int(input('digite outtro numero : '))

if num1 > num2:
    print('o primeiro valor é maior')
elif num2 > num1:#condicao aninhada
    print('o segundo valor é maior')
else:
 print('Não existe valor maior, os dois são iguais.')
