nota1 = float(input('quanto voce tirou em matematica? : '))
nota2 = float(input('quanto voce tirou em portugues? : '))
media = (nota1 + nota2) /2

if media < 5 :
    print('reprovado')
elif media == 5 or media < 7:
    print('reuperacao')
else:
    print('aprovado')