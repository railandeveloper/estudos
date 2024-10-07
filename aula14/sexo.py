sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo : (M/F): ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('O valor está errado, digite novamente.')

print(f'O valor {sexo} está correto.')
print('Fim')

