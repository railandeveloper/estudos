frase = 'railan santos'

# Imprime o primeiro caractere da string
print(frase[0])

# Imprime os caracteres do índice 0 ao índice 12 (13 caracteres no total)
print(frase[0:13])

# Imprime os caracteres do índice 0 ao índice 12, pulando de dois em dois caracteres
print(frase[0:13:2])

# Imprime os caracteres do início da string até o índice 4
print(frase[:5])

# Imprime os caracteres do índice 10 até o final da string
print(frase[10:])

# Imprime os caracteres do índice 2 até o final da string, pulando de três em três caracteres
print(frase[2::3])

print(len(frase)) # para exibir a quantidade de cacacteres em frase

print(frase.count('a'))# para exibir a quantidade de 'a' minusculos na variavel

print(frase.count('a', 0,5))# para exibir a quantidade de 'a' do indice 0 ao 5

print('lan' in frase)#para exibir se existe a palavra 'lan' dentro da variavel




