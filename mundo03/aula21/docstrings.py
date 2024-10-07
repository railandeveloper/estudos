def contador(inicio, fim, passo):  # parametros real
    """_summary_ Função que conta de um número de início até um número final, incrementando de acordo com o passo.
    Args:
        inicio (_type_): O valor inicial da contagem.
        fim (_type_): O valor final da contagem.
        passo (_type_):  O valor a ser incrementado a cada passo na contagem.
    """
    cont = inicio
    while cont <= fim:
        print(f'{cont}', end=' ')
        cont +=passo#vai atribuindo o valor de passo ao cont ate ser maior que fim


contador(2, 10, 2)  # parametro formal
#para ter o manual da funcao criada
help(contador)
