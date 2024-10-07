'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''

# Inicializa duas variáveis para armazenar o maior e o menor peso
# Começamos com None porque ainda não temos nenhum peso lido
maior_peso = 0
menor_peso = 0

for pessoa in range(1, 6):
    peso = float(input(f'Digite seu peso pessoa {pessoa}: '))
    
    if pessoa == 1:
        # Na primeira iteração, inicializamos os dois valores
        maior_peso = peso
        menor_peso = peso
    else:
        # Nas iterações subsequentes, comparamos para encontrar o maior e o menor peso
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso foi {maior_peso:.2f}')
print(f'O menor peso foi {menor_peso:.2f}')