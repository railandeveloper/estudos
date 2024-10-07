def teste(b):
    a = 8#e criada uma variavel a local, que troca somente o valor nesse escopo, a variavel a que esta la em baixo e 5, continua sendo 5 fora desse escopo
    b += 4
    c = 2
    print(b)  # escopo local
    print(f'a variavel a vale {a}')
    print(f'a variavel b  vale {b}')
    print(f'a variavel c vale {c}')

#programa principal
a = 5  # por mais que eu altere os valores dentro de teste, essa variavel global n mudara
teste(a)
print(f'a variavel a vale {a}')
