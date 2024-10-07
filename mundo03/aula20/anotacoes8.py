def dobra(lista):
    posicao = 0
    while posicao <len(lista):#enquanto a posicao for menor que o tamanho da lista
        lista[posicao] *=2# recebe o dobro dela
        posicao +=1
 

valores = [7, 2, 5, 0, 4]
dobra(valores)        
print(valores)    