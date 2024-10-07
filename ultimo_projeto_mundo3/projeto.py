import modulo
import time

lista_pessoas = list()
pessoa0 = {'nome': 'Ana paula vieira', 'idade': 32}
pessoa1 = {'nome': 'Claudio Mendonça', 'idade': 18}
pessoa2 = {'nome': 'Gustavo luiz', 'idade': 40}
pessoa3 = {'nome': 'joao lukas', 'idade': 33}
pessoa4 = {'nome': 'railan santos', 'idade': 26}

    
lista_pessoas.extend([pessoa0, pessoa1, pessoa2, pessoa3, pessoa4])


while True:
    modulo.exibir_menu()
    opcao_usuario = int(input('Sua opção: '))
    if opcao_usuario == 1:
      modulo.mostrarPessoas(lista_pessoas)
      
    elif opcao_usuario == 2:
        modulo.exibirLinha('NOVO CADASTRO')
        nova_pessoa = dict()
        nova_pessoa['nome'] = str(input('Nome: '))
        try:
            nova_pessoa['idade'] = int(input('idade: '))
            lista_pessoas.append(nova_pessoa)
            print(f'Novo registro de {nova_pessoa["nome"]} Adicionado')
        except ValueError:
           print("\033[31mDigite um número válido\033[0m")
           
    elif opcao_usuario < 1 or opcao_usuario > 3:
         print("\033[31m Opcao invalida \033[0m")
    else:
        break

modulo.exibirLinha('Saindo do sistema...')
time.sleep(2)
print('Ate logo!')    
        
           
