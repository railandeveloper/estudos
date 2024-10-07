peso = float(input('digite seu peso (kg) : '))
altura = float(input('digite sua altura : '))
imc = peso / (altura*altura)

print(f'Seu IMC é: {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc >=40:
    print('Obesidade mórbida')
else:
    print('erro no calculo,reinicie o programa')
