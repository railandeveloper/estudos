'''Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.'''

number = int(input('digite um numero para exibir sua tabuada : '))
for comando in range (1,11):
    soma = number * comando
    print(f'{number} x {comando} = {soma}')
   
   
   
   