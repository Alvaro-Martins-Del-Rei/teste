"""
Exercício
peça ao usuário para digitar o seu nome
peça ao usuário para digitar a sua idade
se nome e idade forem digitados:
   exiba:
       seu nome é {nome}
       seu nome é invertido é {nome invertido}
       seu nome contém (ou não) espaços
       seu nome tem {n} letras
       a primeira letra do seu nome é {letra}
       a última letra do seu nome é {letra}
se nada for digitado em nome ou idade:
    exiba:
        desculpe, voce deixou campos vazios
"""
nome = input('Digite seu nome completo: ')
idade = input('Digite a sua idade: ')

if nome and idade:

    print(f'Seu nome é: {nome}')
    print(f'Seu nome ao contrário é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
        
    else:
        print('Seu nome não contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')