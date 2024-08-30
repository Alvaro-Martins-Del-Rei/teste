"""
Formatação básica de strings
s - strings
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direira
^ - centro
sinal - + ou -
= - força o sinal a aparecer antes dos números  
ex.: 0>-100,.1f
conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #botando espaços a esquera da variável "variavel"
print(f'{variavel: <10}.') #botando espaços a direita da variável "variavel"
print(f'{variavel: ^10}.') #botando espaços para deixar a variável "variavel" no centro
#vc pode colocar qualquer valor dps dos ":" para mostrar na tela, mas lembre-se
#não pode ter espaços dps dos : tem q ser assim "variavel:4>10", sempre será assim

print(f'{1000.433435433:0>+10,.1f}')
#a vírgula dps do 10 significa q é pro python mostrar caso o número foi mais ou igual a 1000
#a vírgula mostrando q é 1000, só pra deixar mais bonitinho
print(f'{1000.433435433:0=+10,.1f}')
#vc tbm pode deixar os números dps do carecter de comparação com "+" ou "-"
#isso serve para mostrar se o número é positivo ou negativo
#mas só vai printar se o número que tiver na f-string for igual ao caracter q vc botou dps dos :

print(f'O hexadecimal de 1500 é {1500:08X}')
#esse é o jeito q vc mostra um hexadecimal de um número com f-strings