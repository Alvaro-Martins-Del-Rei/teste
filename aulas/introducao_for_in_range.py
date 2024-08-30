texto = input('Digite qualquer coisa,'
              ' vamos colocar asteriscos entre os caracteres: ')
novo_texto = ''

#o for é beem mais tranquilo que o while, geralmente usamos o for para coisas q nós sabemos
#quando termina e o while, para quando não sabemos quando termina, tipo repetições de digitação de senha

for letra in texto: #para cada letra em texto: (iteração no for)
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*') #fazendo aquele mesmo programa que fizemos com while
print('Acabou o 1° programa\n')


print('Aqui começa o 2° programa\n')
"""
for + range
range -> range(start, stop, step) - o range tbm é um iterável
o range não depende do for e nem o for depende do range
"""
nums = range(10, 0, -1) #se eu boto só um valor no range eu to dando o valor de stop
              #aí o start vira 0 e o step vira 1, +/- assim
              #range(0, valor digitado, 1)
              #tome cuidado com o step negativo, ele funciona apenas para números negativos
              #ou quando vc quiser mostrar o conteúdo de em ordem decrescente

for num in nums:
    print(num)

print('Acabou o 2° programa\n')

print('Entendendo como o laço "for" funciona\n')

"""
iterável -> str, range, etc (__iter__)
iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""
texto = 'Álvaro' #iterável
iterador = iter(texto) #iterator

while True:
    try:
        letra = next(iterador)
        print(letra) #o next vai trazer o próximo valor disponível dentro do iter
    except StopIteration:
        break
        #quando os valores esgotam aparece um erro(StopIteration) na tela
        #tipo quando vc bota 1 printa mais do q o tamanho da string
print('\n')
#esse laço é como o for funciona debaixo dos panos
#para usar o for seria assim:
print('Usando o for para fazer a mesma coisa q o while de cima')
for letra in texto:
    print(letra)