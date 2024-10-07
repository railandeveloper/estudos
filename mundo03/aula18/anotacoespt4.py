galera = list()
dados = list()
maior = menor = 0
#vou ler nome e idade e jogar na estrutura dados
for contador in range(0, 3):
    dados.append(str(input('Nome : ')))
    dados.append(int(input('Idade : ')))
    galera.append(dados[:])
    dados.clear()

for pessoa in  galera: 
    if pessoa[1] >=18:#se idade for maior 
        maior+=1
        print(f'{pessoa[0]} é maior de idade  ')
    else:
        menor+=1
        print(f'{pessoa[0]} e menor de idade') 
print(f'ao todo {maior} sao maiores e {menor} sao menores')