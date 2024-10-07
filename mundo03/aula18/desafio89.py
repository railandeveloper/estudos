#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

dados_alunos = list()

while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Nota 1 : '))
    nota2 = float(input('Nota 2 : '))
    dados_alunos.append([nome, nota1, nota2])
    
    resposta_usuario = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    
    if resposta_usuario == 'N':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')

for indice, valor in enumerate(dados_alunos):
    media = (valor[1] + valor[2]) / 2
    print(f'{indice:<4} {valor[0]:<10} {media:>8}')

while True:
    aluno_escolhido = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))  
     
    if aluno_escolhido == 999:
      break
    
    if aluno_escolhido < len(dados_alunos):
      print(f'as notas de {dados_alunos[aluno_escolhido][0]} são {dados_alunos[aluno_escolhido][1]} e {dados_alunos[aluno_escolhido][2]}')
    else:
        print("Índice de aluno inválido. Tente novamente.")
print('fim do programa')     
    