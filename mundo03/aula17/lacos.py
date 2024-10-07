num = [2,5,9,1]
num[2] = 3
num.append(7)#adicione o 7 ao final da lista
num.sort(reverse=True)#coloque a lista em ordem do maior para o menor
num.insert(2, 0)#adcione o 0 na posicao 2
num.pop()#remove o ultimo elemento
print(num)
print(f'Essa lista tem {len(num)} elementos ')