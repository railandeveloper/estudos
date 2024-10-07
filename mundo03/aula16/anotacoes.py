# variaveis compostas, (tuplas)
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[2])

# aqui ele vai mostrar o primeiro indice, e vai ate o segundo indice, porem ele ignora o segundo e mostra o anterior
print(lanche[0:2])

print(lanche[1:])  # começa no indice 1 e vai ate o ultimo indice

print(lanche[-1])  # exibe o ultimo elemento

print(lanche[-2])  # exibe o penultimo elemento

print(len(lanche)) # len mostra o comprimento da tupla

# primeiro lanche sera o hambueguer, ai faz o looping, segundo lanche seria o  suco  ai faz o looping...
for comida in lanche:
    # ele vai imprimir cada comida da variavel laanche fazendo um looping ate o ultimo lanche
    print(comida)
    
#lanche = () [] {}# 3 formas de iniciarmos uma variavel composta 
''' () tupla
    [] lista
    {} dicionario
'''
    
    
