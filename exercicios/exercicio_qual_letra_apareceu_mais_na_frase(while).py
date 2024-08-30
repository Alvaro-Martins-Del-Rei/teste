frase = 'O Python é uma linguagem de proggramação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'
#quando uma qtde de letras é a mesma o nosso algoritmo sempre mostra a primeira que apareceu delas

i = 0
qtde_mais_vezes = 0
qtde_letra = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtde_mais_vezes_atual = frase.count(letra_atual)

    if qtde_mais_vezes < qtde_mais_vezes_atual:
        qtde_mais_vezes = qtde_mais_vezes_atual
        qtde_letra = letra_atual

    i += 1

print(f'A letra que apareceu mais vezes foi "{qtde_letra}" que apareceu {qtde_mais_vezes}x')