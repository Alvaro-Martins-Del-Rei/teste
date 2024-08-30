"""
listas em python
tipo list - mutável
suporta vários valors de qualquer tipo
conhecimentos reutilizáveis - índices e fatiamento
métodos úties:
    append - adiciona um item ao final
    insert - adiciona um item no índice escolhido
    pop - remove do final ou do índice escolhido 
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena a lista
Create Read Uptade Delete = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Álvaro')
nome = lista.pop()
lista.append(1233)
del lista[-1]
#lista.clear()
lista.insert(0, 'Álvaro') #o .insert recebe 2 argumentos (índice desejado, o que vc quer adicionar), e vc pode colocar qualquer tipo, str, int, float, vc q escolhe
#se colocarmos um númeri de i muito grande ele vai ver qual o último i da lista e vai por o insert no final
#ele vai levar em consideração o número de i, mas se a lista for muito curta o python vai fzr o que eu falei acima
print(f'{lista}\n')

print('Concatenando e estendo listas:\n')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b #a concatenação aqui com o sinal de "+" funciona igual com strs
print(lista_c)
lista_d = lista_a.extend(lista_b) #ja aqui quando printamos a lista_d ela da none pois,
#o extend trabalha encima da lista_a, por isso ele não retorna nada quando colocamos isso dentro de uma variável
#por isso não podemos colocar ese método dentro de outra variável, pois vai trabalhar diretamente com a variável q vc pôs o ".extend"
print(lista_d)