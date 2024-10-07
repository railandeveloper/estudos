import time
def contador(inicio, fim, passo):
    print('-='*30)
    print(f'contagem de {inicio} ate {fim} pulando de {passo} em {passo}')
    
    if inicio < fim:
        for contagem in range(inicio, fim+1, passo):   
            print(contagem, end=' ')
            time.sleep(0.5)
        print()
        
    else:
        if passo > 0:#se o inicio for maior que o fim, e passo for maior que 0
            passo =-passo
        for contagem in range(inicio, fim+1, passo):   
            print(contagem, end=' ')
            time.sleep(0.5)
        print()
        print('-='*30)
            
contador(1, 10, 1)
contador(10, 0, -2) 
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Inicio: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
contador(inicio, fim, passo)

