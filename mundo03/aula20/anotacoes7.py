def contador(*num):
    # variavel tamanho recebe o tamanho de num, que no caso é quantos elementos tem em num
    tamanho = len(num)
    print(f'recebi os valores {num} e sao ao todo {tamanho} numeros')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
