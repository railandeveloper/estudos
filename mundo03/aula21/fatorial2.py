def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):#para calcular o fatorial
       f *= contador # f recebe f, vezes o contador  
    return f 

numero = int(input(f'digite um numero: '))
print(f'o fatorial de {numero} é {fatorial(numero)}')