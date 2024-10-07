# podemos juntar tuplas listas e dicionarios

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
print(locadora)
print(locadora[0]['ano'])  # Isso imprimirá 1977
print(locadora[2]['titulo']) # Isso imprimirá matrix

'''Ou, alternativamente, você pode usar extend para adicionar todos os filmes de uma vez:

locadora = list()
locadora.extend([filme, filme2, filme3])

print(locadora[0]['ano'])  # Isso imprimirá 1977'''
