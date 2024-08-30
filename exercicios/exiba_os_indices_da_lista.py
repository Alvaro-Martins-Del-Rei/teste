"""
for in com listas
"""
lista = ['Álvaro', 'Fernanda', 'Caio']
lista.append('Lombrado')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))