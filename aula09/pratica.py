frase = 'o palmeiras é grande'
print(frase[3])

print(frase.count('o'))  # para contar quantos o minusculo tem na string

# primeiro transformou a string em maiscula, e com o count verificou quantas letras o maiusculas tem na string
print(frase.upper().count('O'))

print(len(frase))  # mostra o tamanho da string

print(frase.replace('grande', 'gigante'))

print('palmeiras' in frase)  # se tem a  palvra palmeiras na variavel

dividio = frase.split()#exibe uma lista da variavel frase, com indices separados
print(dividio[1])# vai exibir a palavra do indice 1 dentro da lista
print(dividio[1] [2]) # aqui pega a palavra do indice 1 da lista e mostra segunda letra


