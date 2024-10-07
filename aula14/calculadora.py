'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

primeiro_valor = int(input('digite o primeiro valor : '))
segundo_valor = int(input('digite o segundo valor : '))

somar  = primeiro_valor + segundo_valor
multiplicar = primeiro_valor * segundo_valor

# Loop principal
while True :
    print('\nEscolha uma opção do menu:')
    print('[ 1 ] somar ')
    print('[ 2 ] multiplicar ')
    print('[ 3 ] maior ')
    print('[ 4 ] novos numeros ')
    print('[ 5 ] sair do programa')

    opcao = int(input('digite o numero da opcao : '))

    if opcao == 1:
        print(f'o resultado é {somar}')
    elif opcao == 2:
            print(f'o resultado é {multiplicar}')
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'{primeiro_valor} é maior que {segundo_valor}, ou seja, o primeiro valor e maior')
        elif primeiro_valor < segundo_valor:
            print(f'{primeiro_valor} é menor que {segundo_valor}, ou seja, o segundo valor e maior')
        else:
            print('os valores sao iguais')
    elif opcao == 4 :
        primeiro_valor = int(input('digite o primeiro valor : '))
        segundo_valor = int(input('digite o segundo valor : '))
    elif opcao == 5:
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida. Tente novamente.')
print('volte sempre ')        
               
        











