"""
faça um programa q peça ao usuário para digitar um número inteiro,
informe se esse número é par ou ímpar. Caso o usuário não digite um número inteiro
informe q esse número não é inteiro
"""

num = input('Digite um número inteiro: ')

try:
    num_int = int(num)
    if (num_int % 2 == 0):
        print(f'O número "{num_int}" é par')
    else:
        print(f'O número "{num_int}" é ímpar')
except:
    print('O número digitado não é um inteiro')