n1 = int(input('digite um valor : '))
n2 = int(input('digite outro valor : '))
n3 = int(input('digite o ultimo valor : '))

menor = n1
if n2 < menor :
    menor = n2
if n3 < menor:
    menor = n3
    
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'o maior valor digitado foi {maior} e o menor foi {menor}')        