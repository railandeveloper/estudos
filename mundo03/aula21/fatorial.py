def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):#para calcular o fatorial
       f *= contador # f recebe f, vezes o contador  
    return f 

resp1 = fatorial(6)
resp2 = fatorial(3)
print(f'o farorial de 6 é {resp1}')
print(f'o fatorial de 3 é {resp2}')  