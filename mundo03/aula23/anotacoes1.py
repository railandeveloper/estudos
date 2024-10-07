'''erros e exceções'''
a = int(input('numerador: '))
b = int(input('Denominador: '))#se for 0, terei uma e xcessao disparada que é o ZeroDivisionError
resultado = a / b
print(f'o resultado é {resultado}')