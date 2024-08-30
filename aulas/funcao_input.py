nome = input('Qual é o seu nome?: ')
#como na função input só entra str, vc precisa fazer aquela coerção vista anteriormente no curso
#caso vc queira fazer uma conta ou mostrar uma idade e essas coisas
print(f'O seu nome é: {nome}')
#caso eu queira mostrar o valor da variável é só botar o sinal de igual dps da variável nas chaves
#como no exemplo abaixo:
print(f'O seu nome é: {nome=}')

#fazendo a coerção do input para int
num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

int_num_1 = int(num_1)
int_num_2 = int(num_2)
#isso é uma forma de fazer a coerção para int, mas a pode dar erro se o usuário digitar letras
#essa verificação nós vamos aprender mais pra frente no curso

print(f'A soma dos números é: {int_num_1 + int_num_2}')