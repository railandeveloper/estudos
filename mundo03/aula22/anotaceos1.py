import uteis

num = int(input('Digite um numero: '))
resultado =uteis.calculoFatorial(num)
resultado_dobro =uteis.dobro(num)
resultado_triplo =uteis.triplo(num)
print(f'o fatorial de {num} é {resultado}. o dobro é {resultado_dobro} e o triplo é {resultado_triplo}')
print(f'o dobro assim é {uteis.dobro(num)}')
print(f'o triplo assim é {uteis.triplo(num)}')
