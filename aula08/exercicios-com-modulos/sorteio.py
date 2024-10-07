# um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele e sortear o nome de forma aleatoria
import random  # para gerar numeros aleatorios
aluno1 = str(input('qual o nome do primeiro aluno? '))
aluno2 = str(input('qual o nome do segundo aluno? '))
aluno3 = str(input('qual o nome do terceiro aluno? '))
aluno4 = str(input('qual o nome do quarto aluno? '))

listaAlunos = [ aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = random.choice(listaAlunos)#para fazer uma escolha dentro da lista
print(f'o aluno sorteado foi {alunoEscolhido}')


