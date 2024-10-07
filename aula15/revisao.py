
while True :
    numero = int(input('gostaria de ver a tabuada de qual numero : ?'))
    if numero < 0:
        break
    contador = 0
    while contador < 10:
        contador +=1
        multi = numero *contador
        print(f'{numero} x {contador} = {multi}')
print('progama encerrado')    
    