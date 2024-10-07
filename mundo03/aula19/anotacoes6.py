pessoas = {'nome': 'railan', 'sexo': 'M', 'idade': 26}

for chave in pessoas.values():#pegue cada chave em pessoas e  mostre o valor 
    print(chave)
    
for chave in pessoas.keys():  #pegue cada chave em pessoas mostre as chaves 
    print(chave)
    
for chave, valor in pessoas.items(): #pegue cada chave e valor de pessoas e mostre
    print(f'{chave} = {valor}')    
    
 # o items quando se trata de dicionario subistitui o enumarete   
    
    