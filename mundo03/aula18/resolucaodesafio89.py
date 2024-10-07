
ficha  = list()

while True:
    nome = str(input('Nome : '))
    nota1 = float(input('nota1 : '))
    nota2 = float(input('nota2 : '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    resposta = str(input('Quer continuar [S/N] ? : ')).strip().upper()
    
    if resposta in  'Nn':
        break
print('-='*30)
  