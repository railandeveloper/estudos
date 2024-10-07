'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')'''


def leiaInt(numero_digitado):  # a msg vai ser o valor de numero
    ok = False
    valor = 0
    while True:
        numero = str(input(numero_digitado))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
           print('\033[0;31m Erro, digite um numero inteiro valido. \033[m')
        if ok:#se o ok for true
               break
    return valor     

numero = leiaInt(f'Digite um numero: ')
print(f'voce acabou de degititar o numero {numero}')
