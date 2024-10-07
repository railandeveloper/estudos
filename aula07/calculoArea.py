largura = float(input('qual a largura da parede?'))
altura = float(input('qual a altura da parede?'))
area = largura * altura
qTdLitro = area / 2 # se um litro de tinta pinta dois metros, e so pegar a quuantidade de metros totais que seria a area , e dividir por 2
print(f'a parede tem {largura} metros de largura e {altura} metros de altura , sendo assim ela tem {area} metros totais')
print(f' é necessario {qTdLitro} litros de tinta para pintar a parede')
