#para ter um somatorio dos numeros
soma = 0

for comando in range(0,3):
    numero = int(input('digite um numero :'))
    soma += numero 
print('fim')
print(f'a soma geral é {soma}')