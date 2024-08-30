"""
cuidados com dados mutáveis
= - copiando o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Álvaro', 'Emily', 1, True, 1.2]
lista_b = lista_a.copy()
#como esses dados são mutáveis quando a gnt cria uma variável igual a outra variável
#ela está apontando para o mesmovalor na memória
lista_a[0] = 'Qualquer coisa' #por isso quando mudamos aqui vai mudar o item na lista
print(lista_a)
print(lista_b)
#ja para listas de tipo imutáveis tempos que usar o .copy