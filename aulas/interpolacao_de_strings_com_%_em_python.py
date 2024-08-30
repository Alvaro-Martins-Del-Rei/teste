"""
Interpolação básica de strings
s - strings
d e i - int
f - float
x e X - hexadecimal(ABCDEF123456789)
"""

nome = 'Álvaro'
preco = 1000.95897643
variavel = '%s, o preço é de: R$%.2f' % (nome, preco)
#a gnt faz essa mesma coisa em C, vc só precisa por os valores das variáveis entre parênteses
#se vc estiver passando mais de uma variável, caso contrário não vai precisar
print(variavel)
print('\nO hexadecimal de %d é %08X' % (1500, 1500))
#nós podemos usar o hexadecimal tanto para trazer as letras minúsculas quanto maiúsculas
#vc pode botar o "0" na frente de um 4(vai puxar as casas mostradas) ou de um 8(msm coisa q o 4)
#o "0" vai preencher as casas q irão faltar no hexa