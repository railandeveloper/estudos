maior_de_idade = 0
homens = 0
mulher_menos_de_vinte = 0 

while True:
    print('-' * 23)
    print('CADASTRE UMA PESSOA')
    print('-' * 23)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    print('-' * 23)
    
    if idade > 18:
        maior_de_idade += 1
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulher_menos_de_vinte += 1
    
    continuidade = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    if continuidade == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maior_de_idade}')
print(f'Ao todo temos {homens} homens cadastrados')  
print(f'E temos {mulher_menos_de_vinte} mulheres com menos de 20 anos')  

        
    

    