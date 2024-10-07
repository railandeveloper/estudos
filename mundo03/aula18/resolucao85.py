'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numero = [[], []]
valor = 0

for contador in range(1,8):
    valor = int(input(f'digite o {contador} valor : '))
    
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
print(f'a lista ficou assim {numero}')
print(f'os numeros pares foram {sorted(numero[0])}')
print(f'os numeros impares foram {sorted(numero[1])}')        