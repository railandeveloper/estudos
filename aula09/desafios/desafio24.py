''' crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com nome 'santo'''


cidade = str(input('Digite o nome da cidade que voce nasceu: ')).strip()

# Verifica se o nome da cidade começa com "Santo", ignorando maiúsculas e minúsculas
if cidade.lower().startswith('santo'):
    # Se a condição for verdadeira, imprime que o nome da cidade começa com "Santo"
    print('O nome da cidade começa com "Santo".')
else:
    # Se a condição for falsa, imprime que o nome da cidade não começa com "Santo"
    print('O nome da cidade não começa com "Santo".')
    
    
#do meu jeito

city = input('digite a cidade que voce nasceu: ').strip()
print('santo' in city)#verifica se foi armazenada a palavra santo na variavel cidade
