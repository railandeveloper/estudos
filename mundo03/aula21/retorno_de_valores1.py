def somar(n1=0, n2=0, n3=0):
    soma = n1 + n2 + n3
    # print(f'a soma vale {soma}'), print limita a um resultado
    return soma


r1= somar(3, 2, 5)#resposta passa a ser 10. pois quando usamos o return, ele armazena o valor no que vem antes da chamada
r2 = somar(1, 7)
r3 =somar(4)
print(f'meu calculos foram {r1}, {r2}, e {r3}')#eu exibo oq vem antes da chamada
