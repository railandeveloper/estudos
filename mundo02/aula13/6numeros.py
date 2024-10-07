soma = 0

for comando in range(1,7):
    numeros = int(input('digite um numero : '))
    if numeros % 2==0:
        soma = soma + numeros
print(f'a soma dos numeros pares é {soma}')