numero = 0
contador = 0
somatorio = 0
escolha_usuario = 'sim'  # Inicialize a variável para entrar no loop
numero_maior = None
numero_menor = None

while escolha_usuario != 'nao':
    contador += 1
    somatorio += numero
    
    numero = int(input('Digite um número: '))
    escolha_usuario = input('Você quer continuar digitando valores? (sim/nao): ').lower()
    
    if escolha_usuario == 'sim':
        media = somatorio / contador
        
        if numero_maior is None or numero > numero_maior:
            numero_maior = numero
        if numero_menor is None or numero < numero_menor:
            numero_menor = numero 
    
    elif escolha_usuario == 'nao':
        print('Programa encerrado')
        print(f'Você digitou {contador} valores')
        print(f'A média dos valores divididos por {contador} é {media:.2f}')
        print(f'O maior número é {numero_maior} e o menor é {numero_menor}')
        break
    else:
        print('Resposta inválida. Por favor, responda "sim" ou "nao".')
print('fim do programa')        

   
    
   
        
    
    
