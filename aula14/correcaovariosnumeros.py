resposta = 'S'
media = 0
somaTotal = 0
contador = 0
maior = 0
menor = 0
while resposta in 'Ss':  # enquanto minha resposta estiver em
    numero = int(input('digite um numero : '))
    contador += 1  # para saber quantos numeros eu digitei
    somaTotal += numero  # para somat todos os numeros
    
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('quer continuar? [S/N] : ')).strip().upper()[0]
    
media = somaTotal / contador    
print(f'acabou, voce digitou {contador} numeros e a media foi {media}')
print(f' o maior valor foi {maior} e o menor valor foi {menor}')

'''media = somatotal / contador'''
