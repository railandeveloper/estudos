# escopo é o local onde a variavel vai existir, e o local onde ela n vai mais existir
def teste():
    x = 8#variavel local, que so pode ser usada dentro de teste
    print(f'na funcao teste , n vale {n}')
    print(f'na funcao teste , x vale {x}')

#programa principal
n = 2#variavel global, pois pode ser usada dentro do teste
print(f'no programa principal, n vale {n}')
#print(f'no programa principal, x vale {x}') a variavel x so existe dentro de teste, por isso ela n funciona, x tem um escopo local

teste()
