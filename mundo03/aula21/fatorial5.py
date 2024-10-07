def parOuImpar(n=0):
    if n % 2 ==0:
        return True
    else:
        return False
    

numero = int(input(f'digite um numero: '))
if parOuImpar(numero):
    print(f'é par')   #Aqui, o código chama a função parOuImpar() passando o número digitado pelo usuário. Se a função retornar True, o bloco de código dentro do if será executado; caso contrário, o bloco dentro do else será executado.
else:
    print(f'é impar')