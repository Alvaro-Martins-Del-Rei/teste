"""
flag(bandeira) - marcar um local
none = não valor
is e is not = é ou não é(tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1)) #para ver o valor q a variável está guardada na memória é só usar o id
print(id(v2)) #quando temos dois valores para a variável igual o py vai por na mesma célula de memória
print(id(v3)) #quando temos diferente vão para lugares diferentes

condicao = True
passou_no_if = None

if condicao:
   passou_no_if = True #essa daqui é a nossa bandeira
   print('\nFaça algo\n')
else:
   print('\nNão faça algo\n')

#e aq a gnt ta verificando essa flag, verificando se passou ou não, se é None ou não
if passou_no_if is None:
   print('Não passou no if')
else:
   print('Passou no if')