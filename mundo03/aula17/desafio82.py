valores = list()
lista_par = list()
lista_impar = list()

while True :
    valor = int(input('digite um valor : '))
    valores.append(valor)
    
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)
        
    usuario = str(input('quer continuar ? : [S/N] ')).strip().upper()
    if usuario == 'N':
        break
  
print(f'A lista completa é {valores}')
print(f'a lista de pares é {lista_par}')
print(f'a lista de impares é {lista_impar}')       
        
    
    