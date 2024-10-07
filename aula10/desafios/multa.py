'''escreva um programa que leia a velocidade de um carro

Se ele ultrapassar 80km/h.moste uma mensagem dizendo que ele foi multado
a multa vai custar 7 reais por km acima do limite'''

velocidade = float(input('digite a velocidade do carro : '))

if velocidade > 80 :
    multa = (velocidade - 80)*7
    # vamos supor que eu passe a 100 por hora, vai ser 100 - 80 =20, e 20 vezes 7
    print(f'voce ultrapassou o limite permitido e foi multado em ${multa:.2f} reais')
else:
    print('Tenha um bom dia! Dirija com Segurança !')
    