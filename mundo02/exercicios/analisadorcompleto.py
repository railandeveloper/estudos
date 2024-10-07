'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
# Inicializamos variáveis para armazenar a soma das idades, o nome do homem mais velho e a idade do homem mais velho
soma_idades = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

# Laço para ler as informações de 4 pessoas
for pessoa in range(1, 5):
    print(f'{pessoa}ª pessoa')
    
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    # Somamos a idade atual à soma total das idades
    soma_idades += idade
    
    # Verificamos se é um homem e se é o mais velho até agora
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    
    # Verificamos se é uma mulher com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calculamos a média de idade do grupo
media_idade = soma_idades / 4

# Exibimos os resultados
print(f'A média de idade do grupo é: {media_idade:.1f} anos')
if nome_homem_mais_velho:
    print(f'O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos')
else:
    print('Não há homens no grupo.')
print(f'Ao todo são {mulheres_menos_20} mulheres com menos de 20 anos')

    
    
  
    
    