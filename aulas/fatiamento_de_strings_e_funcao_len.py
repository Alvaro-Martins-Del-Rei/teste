"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
fatiamento [i:f:p] [::]
obs.: a função len retorna a quantidade de caracteres da string
"""
variavel = 'Olá mundo'

print(variavel[4:]) #em python se vc quiser q o fatiamento mostre até o final é só vc omitir o final
#caso contrário ele vai pegar o índice anterior do índice q vc botou como final
#como nesse exemplo aqui
print(variavel[4:8]) #vc viu q ele mostrou a letra q está no índice 7 invés do 8
#isso serve tbm para se caso vc queira q ele para num determinado índice
#aí vc sempre vai pegar um índice a mais daquele q vc quer mostrar
print(len(variavel[3]))
#a função len vai te retornar a qtde de caracteres q vc tem dentro da variável
#pode ser usada com outras coisas além de str, mas vamos usar só com str por enquanto
#quando vc botar algum índice pra variável puxar o len sempre vai retornar 1
#caso contrário irá mostrar a qtde de carecteres na variável
print(variavel[0:len(variavel):1])
#aí nesse trecho ta falando o seguinte:
#vai começar no índice 0:vai ler a variável até o seu último índice:vai dar passos de 1 em 1
#o passo q vem dps do final vai falar de quantos em quantos carecteres ele vai pular
#o mais comum sendo de 1 em 1
print(variavel[-1:-10:-1])
#isso serve para vc ver a sua str ao contrária
#se vc botar q nem na linha de código de print ali em cima e botar -1 como passo
#ela não vai mostrar nada, pq vc precisa botar os índices negativos tbm

#mas vc pode deixar assim tbm se quiser:
print(variavel[::-1])
#vai dar na mesma coisa