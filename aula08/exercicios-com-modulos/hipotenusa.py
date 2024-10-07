#faca um programa que leia o comprimeto do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimemto da hipotenusa
import math
oposto = float(input('comprimento do cateto oposto '))
adjacente = float(input('comprimento do cateto adjacente '))
hipotenusa = math.hypot(oposto, adjacente)#faz os calculos matematicos para calcular hipotenusa usando o hypot
print(f' o valor da hipotenusa é {hipotenusa:.2f}')