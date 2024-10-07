# variaveis compostas,
# dicionarios

# criando lista
# dados = list()
# adcionado valores a lista
# dados.apend('pedro')

# tuplas()
# listas[]
# dicionarios{}

# nesse caso o valor é pedro, e nome é o identificador(indice) do elemento
dados = {'nome': 'pedro', 'idade': 25}
print(dados['nome'])  # nome seria o indice 0, ou seja, vai imprimir pedro
print(dados['idade'])  # 25

# nos casos de dicionario n e necessario(nao funfa) usar o append para adcionar elementos

# para criar um novo elemento
# vai ser criado o elemento sexo no final do dicionario com o valor 'M'
dados['sexo'] = 'M'
print(dados)

#para remover elementos no dicionario
del dados['idade']
print(dados)
