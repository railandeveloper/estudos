print('-'*25)
print('LOJA SUPER BARATAO')
print('-'*25)

total_compra = 0
produto_acima_De_mil = 0
produto_mais_barato =float('inf')
nome_produto_mais_barato = ''
while True :
    nomeProduto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    print('-'*25)
    
    if preco > 1000:
        produto_acima_De_mil += 1
     
    if preco < produto_mais_barato :
        produto_mais_barato = preco
        nome_produto_mais_barato = nomeProduto
     
    continuidade = str(input('Quer continuar? [S/N] ')).strip().upper()
    total_compra = total_compra + preco
    if continuidade == 'N':
        break
print(f'o total de compras foi R$ {total_compra} reais')
print(f' temos {produto_acima_De_mil} produtos custando mais de R$ 1000.00 reais') 
print(f' e o produto mais barato foi o {nome_produto_mais_barato} que custa R$ {produto_mais_barato} reais')  
    
  