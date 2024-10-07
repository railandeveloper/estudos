texto = 'railan santos'

# funcionalidades de tranformacao

print(len(texto))# para verificar o tamanho da variavel

print(texto.replace('santos', 'aparecido'))
# replace seria trocar ou reoposicionar, no codigo ele ira procurar por 'santos' e ira substituir por 'aparecido'

print(texto.upper())  # para deixar tudo em letras maiusculas

print(texto.lower())  # para deixar tudo em minusculas

# o capitalize pega toda a string e joga tudo para minusculo, e colocar a primeira letra em maiusculo
print(texto.capitalize())

print(texto.title())  # o tile deixa a primeira letra apos o espaço em maiusculo

# o strip remove todos os espacos inuteis antes ou apos o texto
print(texto.strip())

print(texto.rstrip())  # o rstrip remove os espacos da direita apos a string

print(texto.lstrip())  # o lstrip remove os espacos da esquerda antes da string
