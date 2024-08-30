"""
listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úteis: append, insert, pop, del, cls, extend, +
"""
#         01234
#        -54321
string = 'ABCDE' #5 caracteres
lista = [123, True, 'Álvaro', 1.2, []] #dentro de uma lista podemos colocar qualquer coisa de qualquer tipo, inclusive uma lista dentro de outra lista 
#essa é a forma mais comum de definir uma lista, mas podemos usar list(nome), maas não é a melhor forma
#print(bool([])) - false

print(lista)
#na lista podemos printar um índice específico que nem em strings, ex: lista[2]
#vai printar o que está no índice 2 da lista
lista[-3] = 'Maria' #mudando o conteúdo do índice 2 da lista, é possível fzr isso se vc quiser
print(lista[2].upper(), type(lista[2])) #podemos usar o upper, pois, o conteúdo do índice 2 da lista é uma str
print(lista)