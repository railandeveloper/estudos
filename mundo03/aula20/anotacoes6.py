# empacotar parametros, python e uma das poucas linguagens que permite issso
# o * é o simbolo de desempacotar, estou dizendo para o python :'
# o cara vai passar varios parametros ai, mas n sei quantos sao, porem sao varios
def contador(*num):
    for valor in num:  # pegue  cada valor em num
        print(valor, end=' ')
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
