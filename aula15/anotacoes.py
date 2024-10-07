numero = 0
contador = 0
soma = 0

while True:
    numero = int(input('digite um numero : '))
    if numero == 999:
        break
    soma = soma  + numero #So vai ser somado se o numero n for 999
print(f'a soma de todos os numeros é {soma}')    