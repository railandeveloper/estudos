preco = float(input('Qual é o preço do produto? R$ '))
desconto = preco * 0.05  # Calcula o valor do desconto (5% do preço)
print(desconto)
preco_com_desconto = preco - desconto  # Calcula o preço com o desconto aplicado
print(f'Com o desconto de 5%, o valor ficará R$ {preco_com_desconto:.2f}')
