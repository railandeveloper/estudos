'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
# Inicializamos variáveis para armazenar a soma das idades, o nome do homem mais velho e a idade do homem mais velho

soma_idades = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for pessoa in range(1, 5):
    print(f'{pessoa}ª pessoa')
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idades = soma_idades+idade
    media_idade = soma_idades /4
    
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 +=1
                
            
            
        
print(f'a media de idade é de {media_idade:.2f} anos')
print(f'o homem mais velho se chama {nome_homem_mais_velho} e tem {idade_homem_mais_velho} anos')
print(f'{mulheres_menos_20} mulheres tem menos de 20 anos')
    