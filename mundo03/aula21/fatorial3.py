def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):#para calcular o fatorial
       f *= contador # f recebe f, vezes o contador  
    return f 

n1 = fatorial(5)
n2 = fatorial(4)
n3 = fatorial()
print(f'o fatorial de 5 é {n1}')
print(f'o fatorial de 4 é {n2}')
print(f'o fatorial de () é {n3}')