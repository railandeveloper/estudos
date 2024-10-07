dados_pessoas = dict()
lista_pessoas = list()
lista_mulheres = list()
lista_pessoas_acima_idade = list()
contador = 0
soma_idades = 0

while True:
    dados_pessoas['nome'] = str(input('Nome: '))
    dados_pessoas['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    dados_pessoas['idade'] = int(input('Idade: '))
    lista_pessoas.append(dados_pessoas.copy())#copia a o dicionario armazenando na lista  permitindo alterar os dados
    contador+=1
    soma_idades += dados_pessoas['idade']
 
    
    if dados_pessoas['sexo'] == 'F':
        lista_mulheres.append(dados_pessoas['nome'])
   
    resposta_usuario = str(input('Quer continuar ? [S/N]: ')).strip().upper()[0]
    if resposta_usuario == 'N':
        break
media_idade = soma_idades / contador    

for valor in lista_pessoas:#pegue cada valor da lista pessoas
    if valor['idade'] > media_idade:
        lista_pessoas_acima_idade.append(valor.copy())
            
print(f'o grupo tem {contador} pessoas ')
print(f'a media de idade é de {media_idade:.2f} anos')    
print(f'As mulheres cadastradas foram {lista_mulheres}')
print(f'Lista das pessoas que estao acima da media : {lista_pessoas_acima_idade}')