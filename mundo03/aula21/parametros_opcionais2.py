def somar(a=0, b=0, c=0):#se por acaso ele n receber parametros, o resultado sera 0
    soma = a + b + c
    print(f'a soma vale {soma}')


somar(3, 2, 5)
somar(8, 4)  # colocando menos parametros, como n foi passado o parametro c, o c passa a ser 0
somar()
somar(b=4, c=2)
