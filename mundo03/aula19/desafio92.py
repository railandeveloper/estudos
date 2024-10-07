dados_pessoa = dict()

dados_pessoa['nome'] = input('Nome: ')
dados_pessoa['ano_nascimento'] = int(input('Ano de Nascimento: '))
dados_pessoa['carteira_trabalho'] = float(input('Número da CTPS (0 não tem): '))
dados_pessoa['idade'] = 2024 - dados_pessoa['ano_nascimento']

if dados_pessoa['carteira_trabalho'] != 0:
    dados_pessoa['ano_contratacao'] = int(input('Ano da contratação: '))
    dados_pessoa['salario'] = float(input('Salário R$: '))
    dados_pessoa['idade_aposentadoria'] = (dados_pessoa['ano_contratacao'] - dados_pessoa['ano_nascimento']) + 35
    print(dados_pessoa)
else:
    print(f'{dados_pessoa["nome"]} não possui CTPS')

for chave, valor in dados_pessoa.items():
    print(f'{chave} tem o valor {valor}')
