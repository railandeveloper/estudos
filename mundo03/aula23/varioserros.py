# tratamento de ERRO


try:  # tente
    a = int(input('numerador: '))
    b = int(input('Denominador: '))
    resultado = a / b
except (ValueError, TypeError):  # se for erro de valor, ou erro de tipo
    print(f'Tivemos um problema com os tipos de dados que voce digitou.')
except ZeroDivisionError:
    print('nao e possivel dividir um numero por 0')
except KeyboardInterrupt:
    print(f'o usuario preferiu nao informar os dados')
except Exception as erro:#a variavel erro armazena o objeto da excessao'erro'
    print(f'o erro encontrado foi{erro.__cause__}')
else:  # deu certo
    print(f'o resultado é {resultado:.1f}')
# lembrando que else e finally sao opcionais, nem sempre e necessario usar
finally:  # finalmente. vai acontecer tanto se der certo ou falhar
    print(f'volte sempre')
