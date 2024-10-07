'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

valores = list()
while True:
    valor = int(input('Digite um valor: '))
    
    #se ja houver o valor na lista de valores
    if valor in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso')
    
    usuario = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if usuario == 'N':
        break

print(f'Você digitou os valores {sorted(valores)}')
