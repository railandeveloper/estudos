lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
del lanche[3]
lanche.pop(3)#normalmente usado para apagar o ultimo indice, porem pode ser colocado outro no parametro
lanche.remove('pizza')#no remove voce indicar o valor que gostaria de remover, e nao o indice
print(lanche)

if 'pizza' in lanche:#se tiver o valor pizza na lista lanche
    lanche.remove('pizza')#remova o valor