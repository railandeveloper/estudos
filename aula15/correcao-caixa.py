print('='*30)
print('{:^30}'.format('Banco panpanamericano'))
print('='*30)

valor_de_saque = int(input('quanto voce quer sacar ? R$ '))

total = valor_de_saque
cedula = 50
total_de_cedulas = 0
while True :
    if total >= cedula:
        total = total - cedula#exemplo, se o total for igual a 100, ele passa a ser 50, e depois passar a ser 0
        total_de_cedulas +=1#toda vez que tirar uma cedula, o total de cedulas recebe um para sabermos quantas cedulas foram tiradas
    else:#caso n de para tirar 50, tenho que verificar a cedular atual
        print(f' o total de {total_de_cedulas} cedulas de {cedula}')
        if cedula == 50:#como eu n consegui tirar 50, Verifica se a cédula atual é de 50 e, em caso afirmativo, a próxima cédula será de 20.
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_de_cedulas = 0    #Reseta o contador de cédulas para a próxima denominação.
        if total == 0:#se o valor total de saque for igual 0
           break     
            