import time

primeiro_valor = int(input('digite o primeiro valor : '))
segundo_valor = int(input('digite o segundo valor : '))
opcao = 0
while opcao != 5:
    print('[ 1 ] somar ')
    print('[ 2 ] multiplicar ')
    print('[ 3 ] maior ')
    print('[ 4 ] novos numeros ')
    print('[ 5 ] sair do programa')
    opcao = int(input('qual e a sua opcao? : '))
    if opcao == 1:
        print(f' o resultado é {primeiro_valor + segundo_valor}')
    elif opcao == 2:
        print(f'o resultado é {primeiro_valor * segundo_valor}')
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print('o primeiro valor e maior')
        elif segundo_valor > primeiro_valor:
            print('o segundo valor e maior')
        else:
            print('os valores sao iguais')
    elif opcao == 4:
        primeiro_valor = int(input('digite o primeiro valor : '))
        segundo_valor = int(input('digite o segundo valor : '))        
    elif opcao == 5:
       print('finalizando...') 
       time.sleep(2)
    else:
        print('opcao invalida')
print('fim do programa')
