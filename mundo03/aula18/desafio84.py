dados = list()  # Cria uma lista vazia para armazenar os dados
pessoas_cadastradas = 0  # Inicializa o contador de pessoas cadastradas
maior_peso = menor_peso = None  # Inicializa as variáveis de maior e menor peso como None
nome_pessoa_mais_pesada = ''  # Inicializa o nome da pessoa mais pesada

while True:
    nome = str(input('Nome: '))  # Recebe o nome da pessoa
    peso = float(input('Digite seu peso: '))  # Recebe o peso da pessoa
    
    dados.append([nome, peso])  # Adiciona a pessoa e seu peso à lista de dados
    pessoas_cadastradas += 1  # Incrementa o contador de pessoas cadastradas
    
    # Verifica se é a primeira pessoa cadastrada para inicializar maior_peso e menor_peso
    if maior_peso is None or menor_peso is None:
        maior_peso = menor_peso = peso
        nome_pessoa_mais_pesada = nome
    else:
        # Atualiza o maior e menor peso, e o nome da pessoa mais pesada
        if peso > maior_peso:
            maior_peso = peso
            nome_pessoa_mais_pesada = nome
        if peso < menor_peso:
            menor_peso = peso
    
    resposta_usuario = str(input('Você quer continuar cadastrando [S/N]? ')).strip().upper()
    
    if resposta_usuario == 'N':  # Se o usuário não quiser continuar, quebra o loop
        break

print('Essas são as pessoas cadastradas com seu peso e nome:')
print(dados)  # Exibe a lista de dados cadastrados
print(f'A pessoa mais pesada se chama {nome_pessoa_mais_pesada} e tem {maior_peso} kg')
print(f'A pessoa mais leve tem {menor_peso} kg')
