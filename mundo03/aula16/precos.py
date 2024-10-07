# 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''print('-'*50)
print('LISTA DE PREÇOS')
print('-'*50)
print('Lapis ................................R$    1.75')
print('Borracha .............................R$    2.00')
print('Caderno ..............................R$   15.90')
print('Estojo ...............................R$   25.00')
print('Transferidor .........................R$    4.20')
print('Compasso .............................R$    9.99')
print('Mochila ..............................R$  120.32')
print('Canetas ..............................R$   22.30')
print('Livro ............................... R$   34.90')
print('-'*50)'''

listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90,)
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')  # 40 espaços centralizados
print('-'*40)
for posicao_item in range(0, len(listagem)):
    if posicao_item % 2 == 0:  # se for par, é o nome do produto
        print(f'{listagem[posicao_item]:.<30}', end=' ')
    else:  # se for impar
        # fcara alinhado a direita com 7posicoes e duas casas decimais
        print(f'R$ {listagem[posicao_item]:>7.2f} ')
print('-'*40)        