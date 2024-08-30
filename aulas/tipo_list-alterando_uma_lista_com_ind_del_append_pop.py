"""
listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimento reutilizáveis - índices e fatiamento
métodos úteis:
    append, insert, pop, del, cls, extend, +
Create Read Update Delete = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40] #valor inicial da lista
lista[2] = 300 #alterando o valor do índice 2
print(lista)
print(lista[2])
del lista[2] #deletando da lista o índice 2
#e quando ele for apagado, obrigatoriamente, todos os índices atrás dele vão se mover pra trás
#ex: i = 3 -> i = 2
lista.append(50)
print(lista)
ultimo_valor = lista.pop() #o pop sempre vai remover o último elemento inserido na lista
lista.append(60)
lista.append(70) #vc usa o append para adicionar mais elementos a lista
#vc até pode adicionar no meio, mas em lista sempre é mais interessante mexer no final dela
lista.pop(3) #vc tbm pode colocar o índice no qual vc deseja remover com o pop
print(lista, 'Removido', ultimo_valor)
print(lista[2])
#evite adicionar ou remover itens de listas muito grandes, mas quando forem pequenas pode fazer isso