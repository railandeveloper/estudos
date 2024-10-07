import random

times = ('palmeiras', 'santos ', 'flamengo',)
indices = random.randint(0,2)#para gerar indices de 0 a 2 aleatoriamente

print(indices)
print(f'o melhor time é o {times[indices]}')