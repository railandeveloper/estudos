''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''

def notas(*notas_alunos, situacao = False):
   dados_aluno = dict()
   dados_aluno['total'] = len(notas_alunos)
   dados_aluno['maior_nota'] = max(notas_alunos)
   dados_aluno['menor_nota'] = min(notas_alunos)
   dados_aluno['media'] = sum(notas_alunos) / len(notas_alunos)
   
   if situacao:
       if dados_aluno['media'] >= 7:
           dados_aluno['situacao'] = 'boa'
       elif dados_aluno['media'] >=5:
           dados_aluno['situacao'] = 'razoavel'
       else:
           dados_aluno['situacao'] = 'pessima'          
   return dados_aluno



resposta = notas(5.5, 9, 10, 6.5, situacao = True)
print(resposta)