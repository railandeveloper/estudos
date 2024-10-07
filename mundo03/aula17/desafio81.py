'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = list()
contador = 0
while True :
    valores.append(int(input('digite um valor : ')))
    contador +=1
    
    usuario = str(input('quer continuar ? : [S/N] ')).strip().upper()
    
    if usuario == 'N':
        break
#usando o len
print(f'voce digitou {len(valores)} elementos')    
print(f'voce digitou {contador} elementos ')
print(f'A lista em ordem decrescente ficou assim: {sorted(valores, reverse=True)}')  

if 5 in valores:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 nao esta na lista')
    