# Entrada do usuário
frase = str(input('Digite uma frase: '))

# Remover espaços e converter para minúsculas
frase_limpa = ''.join(frase.split()).lower()

# Verificar se a frase limpa é um palíndromo
if frase_limpa == frase_limpa[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
