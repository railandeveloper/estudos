sexo = str(input('digite seu sexo : [ M / F ] :')).strip().upper()[0]#o [0] é para se caso ele digitar a palavra inteira, pegar apenas a primeira letra
while sexo not in 'MmFf':#enquanto sexo nao estiver em :
    sexo = str(input('dados invalidos, por favor digite seu sexo novamente : [ M / F ] : ')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso')    