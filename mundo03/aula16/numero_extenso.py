numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True :
        entrada_usuario = int(input('digite um numero de 0 a 20 : '))
        if entrada_usuario > 20 or entrada_usuario < 0:
          print('tente novamente')
        else:
                break
print(f'voce digitou o numero {numeros[entrada_usuario]}')
    
    

