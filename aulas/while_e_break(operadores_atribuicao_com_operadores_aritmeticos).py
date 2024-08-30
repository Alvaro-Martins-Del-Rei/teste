"""
repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual é o seu nome?: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair': 
        break #sem esse bloco de código o while estava infinito
        #esse break em C, hmm, se tu usa break em C, pode parar de usar já

print('Acabou\n') #essa linha só apareceu pq com o sair teve o break ali
#essa acima éuma forma de fazer while, parando com break
#agora outr forma de fazer while


print('Aqui começa o segundo código\n')


'''
os operadores são:
= -= += *= /= //= **= %=
'''

contador = 0

while contador <= 100: #isso vai fazdr que o contador print até 11
    #nunca ponhe um continue aqui, NUNCA
    contador += 1 #esse é um dos operadores aritméticos q podemos usar, facilita muito o código
                  #e cuidado com essa linha de código, pois ela q ta fazendo o laço funcionar
                  #sem ela nada funciona, por isso não ponha um continue antes dela
    
    if contador == 6:
        print(f'Não vou mostrar o {contador}')
        continue #ele vai ler esse continue e vai voltar para o início do laço
                 #ele sempre vai fazer isso, ele não printa o 6 por causa do continue
                 #o continue sempre faz voltar pro começo do laço, e o print ta antes do break

    if contador >= 10 and contador <= 27: #só pra dar uma reforçada no continue, pra entender
        print(f'Não vou mostrar o {contador}')
        continue #nunca ponhe um continue logo dps de fazer um while, vou mostrar ali antes dos contador += 1
    
    print(contador)

    if contador == 40:
        break #parando o código forçado
#o break e o continue funcionam no while q estiver mais próximo a eles
#quando vc tem um while dentro de um while, eles vão funcionar para o while de dentro

print('Acabou\n')

#Continuando com o conteúdo de while
#agr while dentro de while
print('Aqui começa o 3° programa\n')

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas: #vendo se a condição 'linha' é verdadeira
    coluna = 1 #setando a váriavel coluna = 1
    while coluna <= qtd_colunas: #vendo se a condição 'coluna' é verdadeira
        print(f'{linha=} {coluna=}') #se for verdadeira vai printar
        coluna += 1 #e somar mais um na variável coluna até ela se tornar falsa
    linha += 1 #quando a coluna for falsa vai somar + 1 a linha e fazer tudo dnv
               #até as duas condições forem falsas


print('Acabou\n')

#agr while com else
print('Aqui começa o 4° programa')

string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break #quando tem um break dentro do while o else NUNCA vai ser executado
        #toda vez q o código passa por todo o while, ele vai executar o else
    print(letra)
    i += 1
else: #o else é como se fosse um break, só q ngm usa ele, pq ele é muito peculiar e raro de ser usado, o break é muito mais eficiente
    print('Não encontrei um espaço na string')
print('Fora do while') #o else é como se fosse isso, mas ele não é, pq esse trecho está fora do while
#e o else é da condição do while