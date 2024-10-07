#crie um programa que leia o nome completo de uma e mostre
# o nome completo com letras maisculas
# o nome completo com letras minusculas
# quantas letras ao todo. sem considerar espacos
# quantas letras tem o primeiro nome

nomePessoa = str(input('digite seu nome completo : ')).strip()#esse strip no final elimina todos os espacos da string
print(f'seu nome em maiusculas é {nomePessoa.upper()}')
print(f'seu nome em minusculas é {nomePessoa.lower()}')
print(f'seu nome tem ao todo {len(nomePessoa) - nomePessoa.count(' ')} letras')# esse -pessoa.count retira os espacos entre as palavras do nomepessoa

primeiroNome = nomePessoa.split()#aqui separou o nome em lista
print(f'seu primeiro nome é {primeiroNome[0]}')
print(f'seu segundo nome é {primeiroNome[1]}')
print(f'seu primeiro nome tem {len(primeiroNome[0])} letras')
