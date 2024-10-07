''' Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

# A expressão é uma lista também, toda string é uma lista
expressao = str(input('Digite a expressão: '))  # Recebe a expressão do usuário e armazena como string
pilha = []  # Cria uma lista vazia chamada "pilha" para controlar os parênteses

for simbolo in expressao:  # Percorre cada caractere na expressão
    # Cada parêntese aberto será adicionado na lista "pilha"
    if simbolo == '(':  
        pilha.append('(')  # Adiciona um parêntese aberto à pilha
    elif simbolo == ')':  # Se encontrar um parêntese fechado
        # Se o tamanho da pilha for maior que 0
        if len(pilha) > 0:  # Verifica se já há um parêntese aberto na pilha
            pilha.pop()  # Remove o último parêntese aberto da pilha
        else:  # Se a pilha estiver vazia
            pilha.append(')')  # Adiciona um parêntese fechado na pilha para indicar erro
            break  # Interrompe o loop, pois a expressão já é inválida

# Se a pilha estiver vazia, todos os parênteses foram fechados corretamente
if len(pilha) == 0:
    print('Sua expressão está válida')  # Mensagem indicando que a expressão está correta
else:
    print('Sua expressão está errada:')  # Mensagem indicando que a expressão está incorreta

