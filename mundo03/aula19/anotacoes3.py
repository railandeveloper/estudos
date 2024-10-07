filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values())  # imprimi apenas os valores da estutura filme
print(filme.keys()) # imprimi os elementos (chaves)(indice)
print(filme.items())# para imprimir os valores e as chaves

for chave, valor in filme.items():#para cada chave e  valor de filme
    print(f'o {chave}  é {valor}')#imprimi e depoiss volta pro looping ate acabar