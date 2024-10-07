
times = (
    'Atlético Mineiro', 'Botafogo', 'Corinthians', 'Cruzeiro', 'Flamengo',
    'Fluminense', 'Grêmio', 'Internacional', 'Palmeiras', 'Santos',
    'São Paulo', 'Vasco da Gama', 'Athletico Paranaense', 'Bahia', 'Ceará',
    'Fortaleza', 'Goiás', 'Red Bull Bragantino', 'Coritiba', 'América Mineiro'
)

for lista in times:
    print(lista)

# Exibir os primeiros 5 colocados do Brasileirão
print(f'Os primeiros 5 colocados do Brasileirão são: {times[0:5]}')
print('='*50)
# Exibir os últimos 4 colocados da tabela
print(f'Os últimos 4 colocados da tabela são: {times[-4:]}')
print('='*50)

# Exibir os times em ordem alfabética
print('Times em ordem alfabética:', sorted(times))
print('='*50)

# Encontrar a posição do Vasco da Gama
posicao_vasco = times.index('Vasco da Gama') + 1
print(f'O Vasco da Gama está na {posicao_vasco}ª posição')
print('='*50)
'''O método index em Python é usado para encontrar a posição (índice) de um item específico em uma lista ou tupla. Quando você chama times.index('Vasco da Gama'), ele procura a string 'Vasco da Gama' na tupla times e retorna a posição (índice) dessa string.'''
