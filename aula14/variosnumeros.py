''' 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

numero = 0
somatorio = 0
contador = 0
while numero != 999:
    numero = int(input('digite um numero : '))
    contador += 1
    somatorio = somatorio + numero

    if numero == 999:
        print('programa enceerrado')
        print(f'voce digitou {contador} numeros diferentes')
        print(f'a soma de todos os numeros digitados é {somatorio - 999}')
        break
    else:
        print('tente novamente')
print('fim do programa')
