def aumentar(preco):
    calculo10 = (preco * 10) / 100
    novo_preco = preco + calculo10
    return novo_preco

def resumo(preco, aumento, reducao):
   calculo_aumento = (preco * aumento) / 100
   novo_preco_aumento = preco + calculo_aumento
   calculo_reducao = (preco* reducao) / 100
   novo_preco_reducao = preco - calculo_reducao
   largura = 50  # Define a largura para centralização
   print('--'*25)
   print('RESUMO DO VALOR'.center(largura))
   print('--'*25)
   print(f'preco analisado:    R${preco:.2f}')
   print(f'Dobro do preco :    R${dobro(preco):.2f}')
   print(f'Metade do preco:    R${metade(preco):.2f}')
   print(f'{aumento}% de aumento:     R${novo_preco_aumento:.2f}')
   print(f'{reducao}% de reducao:     R${novo_preco_reducao:.2f}')
   print('--'*25)
   
   
def diminuir(preco):
    calculo13 = (preco*13) / 100
    novo_preco = preco - calculo13
    return novo_preco


def dobro(preco):
    return preco * 2

def metade(preco):
    return preco /2


def leiaDinheiro(preco_digitado):
    valor =0
    ok = False
    while True:
        preco = str(input(preco_digitado))
        if preco.isnumeric():
            valor = int(preco)
            ok = True
        else:
            print(f'\033[0;31m Erro, {preco} é um preço invalido. \033[m')
        if ok == True:
                break
    return valor


