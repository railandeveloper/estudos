'''crie um programa que leia o nome de uma pessoa e diga se ela tem 'silva no nome'''



nome = str(input('Digite seu nome: ')).strip()
nome_minusculo = nome.lower()
print('silva' in nome_minusculo)

if 'silva' in nome_minusculo:
    print('Seu nome tem a palavra "Silva".')
else:
    print('Seu nome não tem a palavra "Silva".')
