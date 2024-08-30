#operadores in e not in
#basicamente in = está entre e not in = não está entre
#Strings são iteráveis
#0 1 2 3 4 5
#Á l v a r o
#-6-5-4-3-2-1

nome = 'Álvaro'
print(nome[2]) #mostrando como trazer a letra no índice que vc desejar colocando o índice desejado entre conchetes
print(nome[-4]) #mostrando a msm coisa do de cima só q com o índice negativo

print( 10 * '-')

print('v' in nome) #o python vai verificar letra por letra e se oq procuramos realmente estar presente na string ele vai retornar True
print('zero' in nome) #vai retornar falso pq não está em

print(10 * '-')

print('v' not in nome) #vai retornar falso pq "v" está em nome
print('zero' not in nome) #vai retornar verdadeiro pq "zero" realmente não está em nome

print(20 * '-')
print('Uma leve brincadeira aqui: \n\n')

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')