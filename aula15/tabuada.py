'''numero = int(input('digite um numero :'))
for contador in range (1,11):
    multi = numero * contador
    print(f'{numero} x { contador} = {multi}')    '''


 
while True:
    numero = int(input('voce quer a tabuada de qual valor ? : ')) 
    if numero < 0:#verfique se o numero  e negativo antes de entrar no loop
        break
    contador = 0#,,contador passa a ser 0 sempre que reinicia, Coloque a inicialização do contador dentro do loop principal, para garantir que ele seja reiniciado a cada nova tabuada.
    while contador < 10:   
        contador +=1 
        multi = numero * contador
        print(f'{numero} x {contador} = {multi}')
print('programa encerrado')        

        
    