'''Desenvolva um programa que pergunte a distancia de uma viagem em km.
calcule o preco da passagem, cobrando 0,50 por km para viagens de ate 200km e 0,45 para viagens mais longas'''

distanciaEmKm = float(input('qual a km percorrida na viagem? :'))


if distanciaEmKm > 200:
    precoPassagem = distanciaEmKm*0.45
    print(f'voce gastou ${precoPassagem:.2f} reais')
else:
    precoPassagem = distanciaEmKm *0.50
    print(f'voce gastou ${precoPassagem:.2f} reais')