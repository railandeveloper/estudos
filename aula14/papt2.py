''' Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('gerador de PA')
print('-=' * 10)

primeiro = int(input('primeiro termo : '))#onde quero começar
razao = int(input('razao : '))#razao seria de quanto em quanto eu quero pular
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total :
        print(f'{termo}')
        termo = termo + razao
        contador += 1
    print('Pausa')
    mais = int(input('quantos termos voce quer mostrar a mais? '))
print('fim')    

    
