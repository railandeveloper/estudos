#tratamento de ERRO


try:#tente 
    #operacao
    a = int(input('numerador: '))
    b = int(input('Denominador: '))#se for 0, terei uma e xcessao disparada que é o ZeroDivisionError
    resultado = a / b    
except:#falhou   
    print(f'infelizmente tivemos um problema :( ')
else:#deu certo
    print(f'o resultado é {resultado:.1f}')
#lembrando que else e finally sao opcionais, nem sempre e necessario usar    
finally:#finalmente. vai acontecer tanto se der certo ou falhar
    print(f'volte sempre')
        
    