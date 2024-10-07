def mostrarPessoas(lista):
    exibirLinha('PESSOAS CADASTRADAS')
    for pessoa in lista :
        print(f'\033[32m{pessoa["nome"].title():<30}\033[0m {pessoa["idade"]} anos')


def exibirLinha(msg):
    largura = 50
    print('-'*50)
    print(f'{msg}'.center(largura))
    print('-'*50)

def exibir_menu():
    exibirLinha('MENU PRINCIPAL')
    print('\033[34m 1 - Ver Pessoas Cadastradas\033[0m')
    print('\033[34m 2 - Cadastrar Nova Pessoa\033[0m')
    print('\033[34m 3 - Sair do sistema\033[0m')
    print('-'*50)
