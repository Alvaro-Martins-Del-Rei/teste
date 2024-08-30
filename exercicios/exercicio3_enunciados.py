"""
faça um programa q peça ao usuário o seu primeiro nome. se o nome tiver 4 letras ou menos
escreva "seu nome é curto"; se tiver entre 5 e 6 letras escreva "seu nome é normal";
maior q 6 letras escreva "seu nome é muito grande"
"""
nome = input('Digite o seu primeiro nome: ')

if len(nome) <= 4:
    print(f'{nome}: Seu nome é curto')

elif len(nome) <= 6:
    print(f'{nome}: Seu nome é normal')

else:
    print(f'{nome}: Seu nome é muito grande')