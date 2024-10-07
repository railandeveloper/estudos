def parOuImpar(n=0):
    if n % 2 ==0:
        resultado = 'par'
    else:
        resultado = 'impar'
    return resultado

numero = int(input(f'digite um numero: '))
print(f'o numero {numero} é {parOuImpar(numero)}')