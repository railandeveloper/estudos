import random

suaEscolha = str(input('Você escolhe pedra, papel ou tesoura? : ')).lower()
escolhaMaquina = random.choice(['pedra', 'papel', 'tesoura']).lower()

if suaEscolha == 'pedra' and escolhaMaquina == 'tesoura':
    print(f'A máquina escolheu {escolhaMaquina}')
    print('Você venceu')
elif suaEscolha == escolhaMaquina:
    print(f'a maquina tambem escolheu {escolhaMaquina}')
    print('empate')
elif suaEscolha == 'tesoura' and escolhaMaquina == 'pedra':
    print(f'A máquina escolheu {escolhaMaquina}')
    print('Você perdeu')
elif suaEscolha == 'papel' and escolhaMaquina == 'pedra':
    print(f'A máquina escolheu {escolhaMaquina}')
    print('Você venceu')
elif suaEscolha =='papel' and escolhaMaquina =='tesoura':
    print(f'A máquina escolheu {escolhaMaquina}')
    print('Você perdeu')
else:
    print('Escolha inválida')
