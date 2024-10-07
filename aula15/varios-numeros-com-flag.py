contador = 0
soma = 0
while True:
    numero = int(input('digite um numero : '))
    if numero == 999:
        break
    contador += 1
    soma  = soma + numero
print(f' foram digitados {contador} valores')
print(f' a soma entre os numeros digitados é {soma}')    
        