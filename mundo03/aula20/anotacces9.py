def somar(*valores):
    soma = 0
    for numero in valores:
      soma += numero
    print(f'somando os valores {valores} temos {soma}')
         
somar(5, 2)
somar(2, 9, 4)
