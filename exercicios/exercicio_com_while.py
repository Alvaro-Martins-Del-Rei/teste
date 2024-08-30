"""
iterando strings com while
"""
nome = input('Escreva o seu nome que o programa vai colocar "*" entre as letras: ') #iteráveis

indice = 0 
novo_nome = '' #atribuindo nada a variavel novo_nome
while indice < len(nome):
    if nome == 'sair':
        print('Programa Encerrado')
        break
    
    else:
        letra = nome[indice] #letra sendo igual ao índice zero do nome
        novo_nome += f'*{letra}' #adicionando * a frente de cada letra
        indice += 1 #adicionando mais 1 ao índice

novo_nome += '*' #adicionando * dps da última letra 
print(novo_nome) #printando a nova str feita