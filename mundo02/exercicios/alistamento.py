'''faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade

se ele ai vai se alistar
se é a hora de se alistar
se ja passou da hora do alistamento'''

anoNascimento = int(input('em que ano voce nasceu? : '))
idade = 2024 - anoNascimento

if idade < 18 :
    print(f'voce ainda ira se alistar pois tem apenas {idade} anos, faltam {18 - idade} anos para o seu alistamento')
elif idade ==18:
    print(f' voce completou {idade} anos, essa é a hora de se alistar')
else:
   print(f'voce tem {idade} anos e ja passou da hora de se alistar, voce deveria ter se alistado {idade - 18} anos atras' )