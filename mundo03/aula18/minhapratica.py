nome = list()
nome.append('railan')
nome.append('joao')
idade = list()
idade.append(26)
idade.append(25)
idade.append(nome[:])#a lista idade recebe uma copia da lista nome e armazena dentro dela
salario = list()
salario.append(1500)
salario.append(5000)
salario.append(idade)
print(salario)
# a lista salario recebe uma copia de idade que ja tinha uma copia de nome