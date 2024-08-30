nome = 'Álvaro Martins Del Rei'
altura = 1.80
peso = 90
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,' #o f significa format
linha_2 = f'pesa {peso:.1f} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'
#isso é uma formatação de strings que podemos fazer para botar variáveis e strings na mesma linha, sem a necessidade de botar aquelas virgulas no print
#o (:.2f) serve para mostrar o número de casas decimais q vc quer printar, por exemplo, duas que nem no exercício

print(linha_1)
print(linha_2)
print(linha_3)