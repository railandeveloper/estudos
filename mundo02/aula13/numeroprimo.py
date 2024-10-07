'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
#o numero primo é diviseivel somente duas vezes
'''exemplo: 13
o numero 13 é divisivel apenas por 1 ou por ele mesmo'''


numero = int(input('digite um numero : '))
total = 0

for contador in range(1, numero + 1):#o numero +1 e pq o python para no numero anterior
    
    if numero % contador ==0:#se o numero for divisivel por 1,2,3..
       print ('\033[33m', end='')#ele tera essa cor
       total +=1#total de vezes que ele e dividido
    else:
        print ('\033[31m',end='')#se nao, ele tera essa cor
    print(contador)
print(f' o numero {numero} foi divisivel {total} vezes')

if total ==2:# numero primo so pode ser diivisivel duas vezes
    print('o numero e primo')
else:
    print('o numero nao e primo')
    