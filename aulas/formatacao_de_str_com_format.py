a = 'A'
b = 'B'
c = 1.1

string = 'a = {nome1}, b = {nome2}, c = {nome3:.2f}' #quando vc for usar o método format vc tem q por o valor da variável entre chaves
#como no exemplo
#se alguma vez dar o erro "out of range", quer dizer q vc está buscando uma coisa q já acabou
formato = string.format(nome1=a, nome2=b, nome3=c) #oq está dentro do parenteses são os argumentos/valores que voce está colocando no format, e quando vc for chamar vc põe entre chaves e vai assim:
#a primeira chave remete ao primeiro valor dentro do format, a segunda chave ao segundo valor e assim via subconsequentemente
#e se vc quiser mostrar casas decimais quando houver números é só por :.2f(como no código) dentro das chaves da variável onde se encontra o número
#tudo em python é objeto
#vc tbm pode por os índices dos valores dentro do format dentro das chaves para ficar mais fácil e vc não ficar dependendo da ordem
#as vezes os índices não podem ser confiáveis, então vc pode nomear as coisas, como lá format lá em cima
#isso é chamado de parâmetro nomeado, ele é mais confiável q o índice para ser usado com o format
print(formato)
#quando uma função está dentro de um objeto ela é chamada de método, mas ela continua sendo uma função