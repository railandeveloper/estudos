numero = 1
impar = 0
par = 0
while numero !=0:
    numero = int(input('digite um numero : '))
    if numero !=0:#se o numero for diferente de 0, para nao contar o 0, ou seja , o 0 nao entrara nessa parte do programa, ele vai somar tudo que n for 0
        if numero %2 ==0:
            par = par + 1
        if numero %2 ==1:
            impar = impar + 1  

print('acabou') 
print(f'{par} numeros sao pares')
print(f'{impar} numemros sao impares')   