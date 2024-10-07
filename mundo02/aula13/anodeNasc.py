# Inicializar contadores
maiores = 0
menores = 0

# Loop para obter as idades de 7 pessoas
for pessoa in range(1, 8):
    anoNasc = int(input(f'Digite o ano de nascimento da pessoa {pessoa}: '))
    idade = 2024 - anoNasc

    # Verificar se a pessoa é maior ou menor de idade
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

# Exibir os resultados
print(f'{maiores} são maiores de idade')
print(f'{menores} são menores de idade')
