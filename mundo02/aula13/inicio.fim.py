inicio = int(input('inicio : '))
fim = int(input('fim : '))
passo = int(input('passo : '))

for comando in range(inicio, fim+1, passo):#execute o comando no intervalo que começa em inicio acaba em fim, e pula de passo em passo. exemplo inicio 0, fim 10, passo 2, vai iniciar em 0 acabar em 10 pulando de duas em duas casas 
    print(comando)
