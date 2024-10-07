def factor(numero, show=None):
    fatorial = 1
    for contador in range(numero, 0, -1):
        if show:  # se show for true
            print(f'{contador}', end=' ')
            if contador > 1:
                print('x', end=' ')
            else:#se for igual a 1
                print('=', end=' ')
        fatorial *= contador
    return fatorial


print(factor(5, show=True))
