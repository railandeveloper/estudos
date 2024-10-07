''''''

anoNascimento = int(input('em qual ano voce nasceu? : '))
idade = 2024 - anoNascimento

if idade <=9 :
    print('mirim')
elif idade <= 14:
    print('infantil')
elif  idade <= 19:
    print('junior')
elif  idade <= 20:
    print('senior')
else:
    print('master')