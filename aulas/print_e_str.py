print(12, 34, sep="-") #quando a gnt botar vírgula nos argumentos do print ele vai dar um espaço automaticamente
#quebra de linha automática
print(56, 78, sep = '-', end = "#\n\n") #sep é o separador e vc q define como q vai ser a sepação dele
#pode ter espaço entre as palavras dele e pode usar aspas simples(') ou aspas duplas("")
#a função end serve para vc ver o vai para o final do print, vc vai vê-lo, pode ser um \n ou outra coisa

"""
Tipagem do python - dinâmina/forte - dinâmica -> o python já sabe qual o tipo de informação q vc ta passando pra ele
str -> string -> textos
Strings são textos q estão dentro de aspas
"""

#Aspas Simples
print('Aspas Simples')
#Aspas Duplas
print("Aspas Duplas")

#esses dois exemplos são mais utilizados, pois deixam o seu código mais limpo
print('Aspas "Duplas"') #aspas duplas dentro de aspas simples pode
print("Aspas 'Duplas'") #aspas simples dentro de aspas duplas tbm pode

#esses dois exemplos não são muito usados, pois são muito complicados
#Escape(caracteres de escape)
print("Aspas \"Duplas\"") #caso eu queira botar uma aspas no meio da str eu tenho que botar \ para pular essa aspas, mas ela vai aparecer na hora de printar
#r(expressões regulares)
print(r"Aspas \"Duplas\"") #caso eu queira q apareça o caracter de escape é só botar o r na frente da frase