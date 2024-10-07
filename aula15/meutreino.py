print('='*30)
print('BANCO PANPANAMERICANO')
print('='*30)

valor_de_saque = int(input('qual valor voce quer sacar ? R$ : '))
valor_total = valor_de_saque
cedula = 50
contador_de_cedulas = 0

while True :
    if valor_total >= cedula:
        valor_total -= cedula
        contador_de_cedulas +=1     
    else:
        print(f'{ contador_de_cedulas} notas de {cedula} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contador_de_cedulas =0
        if valor_total == 0:
            break
print('orbigado por comparecer no nosso banco ')                    