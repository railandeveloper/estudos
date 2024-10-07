'''Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''

def leiaInt(msg):
    while True:
        numero = str(input(msg))
        if numero.isnumeric():
            valor = int(numero)
            return valor
        else:
            print('Erro: Digite um número inteiro válido.')
            
        
def leiaFloat(msg):
    while True:
        numero = input(msg)
        try:
            valor =float(numero)
            return valor
        except ValueError:
           print('Erro: Digite um número real válido.')
    
        
numero_inteiro = leiaInt('Digite um inteiro: ')
numero_real = leiaFloat('Digite um Real: ')
print(f'o valor inteiro digitado foi {numero_inteiro} e o real foi {numero_real}')

    
    