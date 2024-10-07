'''faca um porgrama que leia o nome de uma pessoa, mostrando em seguida o primeiro e o ultimo nome independente do tamanho do nome
ex:ana maria souza
primeiro:maria
ultimo:souza'''

nomeCompleto = str(input('Digite seu nome Completo : ')).strip()
divisaoDeNome = nomeCompleto.split()
primeiroNome = divisaoDeNome[0]
ultimoNome = divisaoDeNome[-1]  # Alteração aqui para pegar o último nome, independente do tamanho do nome
print(f'Seu primeiro nome é: {primeiroNome}')
print(f'Seu último nome é: {ultimoNome}')

'''
Claro! Em Python, usar o índice -1 em uma lista significa "pegar o último item". Isso acontece porque Python conta os índices de trás para frente, começando do -1 para o último elemento, -2 para o penúltimo, e assim por diante. É uma maneira conveniente de acessar o último item de uma lista sem precisar saber o tamanho total da lista. Então, ao usar divisaoDeNome[-1], você está dizendo ao Python para pegar o último nome da lista divisaoDeNome, não importando quantos nomes existam na lista.'''

