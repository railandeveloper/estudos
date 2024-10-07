#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
base = int(input('Escolha a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal: '))

if base == 1:
    print(f'O número {numero} em binário é: {bin(numero)}')
elif base == 2:
    print(f'O número {numero} em octal é: {oct(numero)}')
elif base == 3:
    print(f'O número {numero} em hexadecimal é: {hex(numero)}')
else:
    print('Opção inválida. Por favor, escolha 1 para binário, 2 para octal ou 3 para hexadecimal.')
