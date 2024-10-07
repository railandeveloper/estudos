diaria = 60
precoKm = 0.15
diasRodados = int(input('quantos dias voce rodou? '))
kmRodados = float(input('quantos km voce rodou? '))
gastoDiaria = diaria * diasRodados
gastoKm = kmRodados * precoKm
gastoTotal = gastoDiaria + gastoKm
print(f'voce deve pagar R$ {gastoTotal} reais')
