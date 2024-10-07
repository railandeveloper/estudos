tempo = int(input('quantos anos tem seu carro? '))
print('carro novo' if tempo <=3 else 'carro velho')
#escreva carro novo se tempo for menor ou igual a 3, se nao, escreva carro velho

idade = int(input('qual a sua idade? : '))
print('menor de idade' if idade <= 17 else 'maior de idade')

nome = str(input('qual é o seu nome? '))
if nome == 'jose':
    print('nome bonito em')
else:
    print('nome fei em')