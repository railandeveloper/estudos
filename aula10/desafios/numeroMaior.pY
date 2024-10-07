'''faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor'''
# Lê os três números do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calcula o maior número usando a função max()
maior = max(num1, num2, num3)

# Calcula o menor número usando a função min()
menor = min(num1, num2, num3)

# Mostra o maior e o menor número
print(f"O maior número é: {maior:.0f}")
print(f"O menor número é: {menor:.0f}")
