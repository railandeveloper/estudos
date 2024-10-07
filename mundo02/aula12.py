#estrutura condiconal aninhada

name = str(input('digitge seu nome : '))
print(f'tenha um bom dia, {name}')
if name == 'railan':
    print(f'que nome bonito {name}')
elif name == 'joao' or name == 'maria' or name == 'pedro':#se nome for igual ou 
    print(f'seu nome é bem popular no Brasil {name}')
elif name in 'ana claudia jessica juliana':#se ena vairvael nome houver alguma dessas palavras 
    print('belo nome feminino')
else:
    print('seu nome e feio')