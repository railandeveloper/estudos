'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('gerador de PA')
print('-=' * 10)
primeiro = int(input('primeiro termo : '))#onde quero começar
razao = int(input('razao : '))#razao seria de quanto em quanto eu quero pular
termo = primeiro
contador = 1

while contador <= 10 :
    print(f'{termo}')
    termo = termo + razao
    contador += 1
    
