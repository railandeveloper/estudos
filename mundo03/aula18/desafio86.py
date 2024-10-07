'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

# dentro de cada indice da matriz eu tenho 3 valores
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):  # PARA CADA LINHA(que sao 3)
    for coluna in range(0, 3):  # HAVERÁ 3 COLUNAS
        matriz[linha][coluna] = int(
            input(f'Digite um valor para [{linha}, {coluna}]: '))


# for de exibicao
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()
