pessoas = {'nome': 'railan', 'sexo': 'M', 'idade': 26}
del pessoas['sexo']#deletando a chave sexo e o valor m
pessoas['nome'] = 'leandro'#mudando o valor da chave nome para leandro
pessoas['peso'] = 80.5 #adcionado a chave peso e o valor 80
for chave, valor in pessoas.items(): #pegue cada chave e valor de pessoas e mostre
    print(f'{chave} = {valor}')    
    