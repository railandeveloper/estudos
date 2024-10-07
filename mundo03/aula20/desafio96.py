'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''


def msg(l, c):
    calculo_area = l * c
    print(f'A área de um terreno de {l}x{c} é de {calculo_area} m²')

print('Controle de Terrenos')
print('-'*20)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
msg(largura, comprimento)

