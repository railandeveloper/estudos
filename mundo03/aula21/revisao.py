def factor(numero, show=None):
    fatorial = 1
    for contador in range(numero, 0, -1):
        if show:
            print(f'{contador}', end='')
            if contador > 1:
                print(f'x', end='')
            else:
                print(f'=', end='')
        fatorial = fatorial *contador
    return fatorial


print(factor(5, show=True))
