def teste(b):
    global a  # Modifica a variável global 'a'
    a = 8  # 'a' global agora vale 8 #A NAO TEM NADA A VER COM O B ALI EM CIMA
    b += 4  # 'b' é uma variável local, sua modificação não afeta a variável global 'a'
    c = 2  # 'c' também é uma variável local
    print(b)  # Imprime 9 (5 + 4)
    print(f'a variavel local a vale {a}')  # Imprime 8 (a global modificada)
    print(f'a variavel b  vale {b}')  # Imprime 9 (valor local de 'b')
    print(f'a variavel c vale {c}')  # Imprime 2 (valor local de 'c')

# Programa principal
a = 5  # Variável global 'a' inicializada com 5
teste(a)
print(f'a variavel global a vale {a}')  # Imprime 8, pois 'a' foi modificada na função 'teste'
