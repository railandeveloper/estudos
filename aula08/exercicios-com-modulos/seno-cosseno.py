#faca um programa qque leia um angulo qualquer e moste na tela o valor do seno, cosseno e tangente desse angulo
import math

angulo = float(input('Digite o ângulo que você deseja: '))

# Convertendo o ângulo para radianos
angulo_rad = math.radians(angulo)

# Calculando o seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Exibindo os resultados
print(f'O ângulo de {angulo} graus tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} graus tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} graus tem a TANGENTE de {tangente:.2f}')
