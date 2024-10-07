numero = (int(input('digite um numero : ')),#os numeros ficrao salvos em uma tupla
            int(input('digite outro numero : ')),
            int(input('digite mais um numero : ')),
            int(input('digite o ultimo numero : ')))

print(f'voce digitou os numeros {numero}')
print(f'o valor 9 apareceu {numero.count(9)} vezes')
if 3 in numero:#se o 3 estiver dentro da tupla numero
    print(f'o numero 3 apareceu na posicao {numero.index(3)}')
else:
    print('o numero 3 n foi digitado')

for n in numero :
    if n % 2 == 0:
        print(f' {n} é par ')

            