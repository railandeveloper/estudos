import time

def maior(*numeros):
    print('-='*30)
    print('Anlisando os valores passados...')
    time.sleep(2)

    print(f'os numeros sao esses {numeros}, temos {len(numeros)} valores ao todo, tendo o  o maior deles sendo o {max(numeros)}')
   
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior(0)    
 