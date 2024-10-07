'''Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}: '))
print(f'nome é igual a {aluno["nome"]}')
print(f'media é igual a {aluno["media"]}')
print(aluno)
if aluno['media'] >=7:
   aluno['situacao'] = 'aprovado'
elif aluno['media'] >=5:
    aluno['situacao'] = 'recuperacao'
else:
    aluno['situacao'] = 'reprovado'

for chave, valor in aluno.items():
    print(f'{chave} é igual a {valor}')
    