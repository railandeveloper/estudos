valor_corrida = float(input('Digite o valor da corrida R$ : '))
tempo_corrida = float(input('Qual o tempo da corrida (em minutos)? '))
quantidade_kms_corrida = float(input('Quantos km você vai rodar? : '))

valor_por_km = valor_corrida / quantidade_kms_corrida
valor_por_min = valor_corrida / tempo_corrida

print(f'A corrida de R${valor_corrida:.2f} Reais, paga R${valor_por_km:.2f} por km rodado e R${valor_por_min:.2f} Reais por minuto')
