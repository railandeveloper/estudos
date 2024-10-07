valores = list()
par = list()
impar = list()
for contador in range (1,8):
    numero = int(input(f'Digite o {contador} valor : '))
    valores.append(numero)
    
    if numero % 2 == 0:
        par.append(numero)
    else:
       impar.append(numero)  
    
print(f'os numeros paress são {sorted(par)}')
print(f'os numeros impares sao {sorted(impar)}') 
    
    
 