def voto(ano_nascimento):
    idade = ano_atual - ano_nascimento
    if idade >= 18 and idade <= 60:
        return 'Obrigatorio'
    elif (idade >= 16 and idade < 18) or idade > 65:
        return 'opcional'
    else:
        return 'negado'



print('-'*20)
ano_nasc = int(input('Em que ano voce nasceu?: '))
ano_atual = 2024
idade = ano_atual - ano_nasc
print(f'com {idade} anos: o voto é {voto(ano_nasc)}')  