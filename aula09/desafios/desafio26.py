'''faça um programa que leia uma frase pelo treclado e mostre
quantas vezes aparece a letra A
em qual posicao ela aparece a primeira vez
em que posicao ela aparece a ultima vez'''

frase = (input('digite uma frase : ')).strip()
mudancaMaisculo = frase.lower()
print(f' a letra "a" aparece {mudancaMaisculo.count('a')} vezes na frase')

# o find e utilizado para verificar em qualk posicao aparece pela primeira vez a letra
print(f'A primeira letra A apareceu na posicão {mudancaMaisculo.find('a')}')

print(f'a ultima letra A apareceu na posiçao {mudancaMaisculo.rfind('a')}')
#rfind verifica a ultima letra da parte direita
