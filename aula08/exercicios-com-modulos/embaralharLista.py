# sorteio de ordem de apresentacao dos alunos
import random

aluno1 = str(input('primeiro aluno : '))
aluno2 = str(input('segundo aluno : '))
aluno3 = str(input('terceiro aluno : '))
aluno4 = str(input('quarto aluno : '))

listaDeAlunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(listaDeAlunos)# o metodo shuffle serve para embaralhar a lista
print(f'A ordem da apresentacao sera {listaDeAlunos}')


