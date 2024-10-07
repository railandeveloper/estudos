
'''O que seria necessário para torná-lo mais avançado?
Para elevar esse código a um nível mais claramente intermediário ou avançado, você poderia:

Modularização: Dividir o código em mais funções para tornar cada parte do processo mais clara e reutilizável.
Tratamento de Exceções: Adicionar tratamento de erros para capturar entradas inválidas (como digitar uma string quando o programa espera um número).
Persistência de Dados: Salvar e carregar a lista de filmes de um arquivo, para que os dados persistam entre as execuções do programa.
Interface Gráfica: Criar uma interface gráfica simples usando uma biblioteca como Tkinter, que traria um desafio adicional e mais complexidade ao projeto.
Portanto, seu código está no caminho certo e já apresenta elementos que vão além do básico. Com algumas melhorias, pode ser facilmente considerado de nível intermediário.
'''
import time

def mostrar_filmes(locadora):
    print('-='*30)
    print(f'Esses são os filmes disponiveis: ')
    for indice, valor in enumerate(locadora):
        print(f'filme {indice}: {valor}')

filme0 = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

filme1 = {
    'titulo': 'Avengers',
    'ano': 2012,
    'diretor': 'Joss Whedon'
}

filme2 = {
    'titulo': 'Matrix',
    'ano': 1999,
    'diretor': 'Wachowski'
}

locadora = list()
locadora.append(filme0)
locadora.append(filme1)
locadora.append(filme2)


while True:
    mostrar_filmes(locadora)
     
    Alugar_ou_devolver = int(input('Digite 0 para alugar um filme ou 1 para devolver um filme: '))
    
    if Alugar_ou_devolver == 0:    
        filme_escolhido = int(input('Qual filme você gostaria de alugar? (Digite o número correspondente): '))
        if filme_escolhido >= 0 and filme_escolhido < len(locadora):
            print(f'voce escolheu o filme: {locadora[filme_escolhido]}')
            locadora.pop(filme_escolhido)
            print('sobraram os filmes')
            mostrar_filmes(locadora)
        else:
           print('Opção inválida. Tente novamente.')  
    else:
         filme_devolvido = str(input('Quer devolver algum filme[S/N]: ')).upper().strip()
         if filme_devolvido == 'S':
            novo_filme = dict()
            novo_filme['titulo'] = str(input('Nome do filme: '))
            novo_filme['ano'] = int(input('Ano do filme: '))
            novo_filme['diretor'] = str(input('Diretor do filme: '))
            locadora.append(novo_filme)
            print('Agora temos os filmes: ')
            print('-='*30)
            mostrar_filmes(locadora)
         else:
             print(f'carregando...')
             time.sleep(2)
           
    reposta = str(input('Quer continuar Alugando[S/N?: ')).strip().upper()
    if reposta == 'N':
        break 
print('-='*30)    
print(f'Volte sempre!')       