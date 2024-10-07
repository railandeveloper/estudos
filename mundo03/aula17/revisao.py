valores = list()

while True :
    valor = int(input('digite um valor : '))
    
    if valor in valores:
        print('valor duplicado, nao irei adicionar ')
    else:
        valores.append(valor)
        print('valor adicionado com sucesso ... ')
    usario = str(input('quer continuar ? : [S/N] : ')).strip().upper()
    if usario == 'N':
        break    
print(f'voce digitou os valores {valores}')

    
        
        