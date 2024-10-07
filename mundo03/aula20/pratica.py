'''aça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
import time

def contador(inicio, fim, passo):
    print(f'vamos iniciar com {inicio} até {fim} pulando de {passo} em {passo} ...')
    time.sleep(2)
    
    if inicio < fim:
        for contagem in range(inicio, fim+1, passo):
            print(contagem, end=' ')
        print() 
    else:
      if passo > 0:
        passo = -passo
      for contagem in range(inicio, fim, passo):
        print(contagem, end=' ')
      print()   
   
contador(1, 10, 1)
contador(10, 0, -2)
print('contagem personalizada...')
inicio = int(input('inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio, fim, passo) 
    
    