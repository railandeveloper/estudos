print('='*20)
print('Banco panpanamericano')
print('='*20)

valor_de_saque = float(input('quanto voce quer sacar ? R$ '))

total = valor_de_saque
cedula = 100
contador_cedulas = 0

while True :
    if total >= cedula:#se o valor total que quero sacar for maior que a cedula
        total = total - cedula
        contador_cedulas +=1
    else:
        print(f'{contador_cedulas} notas de {cedula}')
        if cedula  == 100:
            cedula = 50#passou a ser 50, faz todo o percurso inical do codigo e assim sucessivamente 
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1 
        contador_cedulas = 0
        if total == 0:
            break
                 