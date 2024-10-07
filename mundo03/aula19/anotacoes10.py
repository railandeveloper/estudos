estado = dict()  # outra forma de criar um dicionario
brasil = list()

for contador in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado : '))
    brasil.append(estado.copy())  # o copy() é usado para fazer uma cópia do dicionário em cada loop e armazenar novos dados

for indice in brasil:#pegue cada indice da lista brasil
    for chave in indice.values():#pegue cada chave em indice e  mostre o valor 
        print(chave)
        
       