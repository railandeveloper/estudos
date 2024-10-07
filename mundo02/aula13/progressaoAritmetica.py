'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

'''for numero in range (0,11,2):#isso aqui seria uma pa. onde o primeiro termo é 0 e  razao é 2
    print(numero)'''
   
    
primeiro = int(input('primeiro termo : '))#onde quero começar
razao = int(input('razao : '))#razao seria de quanto em quanto eu quero pular
decimoTermo = primeiro + (10 - 1) * razao#formula para calcular o decimo termo

for contador in range(primeiro,decimoTermo, razao):
    print(f'{contador}', end=' → ')
  
#primeiro termo é onde quero começar , razao é de quanto em quanto quero pular    