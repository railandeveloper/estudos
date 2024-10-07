# criando um dicionario dentro de uma lista

brasil = []  # criei brasil como uma lista
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}  # estado1 como dicionario
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}  # estado2 como dicionario
brasil.append(estado1)  # devo adcionar um dicionario por vez
brasil.append(estado2)

print(brasil[0])#vai imprimir o elemento de inidce 0 da lista brasil
print(brasil[0]['uf'])
print(brasil[1] ['sigla'])