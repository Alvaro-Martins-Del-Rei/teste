"""
faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito
exiba a saudação apropriada. Ex:
Bom dia(0 - 11), Boa tarde(12 - 17), Boa noite(18 - 23).
"""

nome = input('Qual o seu nome?: ')
horario = input('Digite um horário como um número inteiro: ')

try:
    horario_int = int(horario)
    if horario_int >= 0 and horario_int <= 11:
        print(f'Bom dia {nome}')

    elif horario_int >= 12 and horario_int <= 17:
        print(f'Boa tarde {nome}')

    elif horario_int >= 18 and horario_int <= 23:
        print(f'Boa noite {nome}')
    
    else:
        print(f'{nome} eu não conheço esse horário')
except:
    print('Você não colocou um número inteiro')