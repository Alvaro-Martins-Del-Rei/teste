import os

palavra_secreta = 'arroz'
letras_acertadas = ''
qtde_tentativas = 0

while True:
    letra_d = input('Digite uma letra: ')
    qtde_tentativas += 1

    if len(letra_d) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_d in palavra_secreta:
        letras_acertadas += letra_d

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era:', palavra_secreta)
        print('Tentativas:', qtde_tentativas)
        letras_acertadas = ''
        qtde_tentativas = 0