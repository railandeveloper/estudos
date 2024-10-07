'''Faça um porograma que leia um ano qualquer e mostre se ele é bissexto'''
# Solicita ao usuário que insira um ano e armazena o valor na variável 'ano'
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto de acordo com as regras estabelecidas
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    # Se a condição for verdadeira, imprime uma mensagem informando que o ano é bissexto
    print(f"{ano} é um ano bissexto.")
else:
    # Se a condição não for verdadeira, imprime uma mensagem informando que o ano não é bissexto
    print(f"{ano} não é um ano bissexto.")


'''ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.'''