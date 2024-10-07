''': Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

# Inicializa uma lista vazia chamada 'lista'
lista = list()

# Loop que será executado 5 vezes (de 1 a 5, inclusive)
for contador in range(0, 5):
    # Solicita ao usuário que digite um valor e converte esse valor para inteiro
    numero = int(input('Digite um valor: '))
    
    # Verifica se é a primeira iteração do loop ou se o número digitado é maior que o último número na lista
    if contador == 0 or numero > lista[-1]:
        # Se for a primeira iteração ou o número for maior que o último número na lista, adiciona o número ao final da lista
        lista.append(numero)
    else:
        # Se o número não for maior que o último número na lista, inicia uma variável 'posicao' em 0
        posicao = 0
        # Loop que percorre a lista para encontrar a posição correta para inserir o número
        while posicao < len(lista):
            # Se o número for menor ou igual ao número na posição atual da lista
            if numero <= lista[posicao]:
                # Insere o número na posição atual
                lista.insert(posicao, numero)#ele insere o numero na posicao 0 e sucess...
                # Sai do loop
                break
            # Incrementa a posição para verificar o próximo elemento na lista
            posicao += 1

# Exibe a lista de números em ordem crescente
print(f'Os valores digitados em ordem foram {lista}')
