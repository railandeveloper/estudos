def calculoFatorial(numero):
    fatorial = 1#nao posso inicilizar o valor com 0, pois qualquer numero multiplicado por 0 é 0
    for contador in range(numero, 0, -1):
        fatorial = fatorial*contador
    return fatorial

def dobro(numero):
    return numero*2


def triplo(numero):
    return numero*3