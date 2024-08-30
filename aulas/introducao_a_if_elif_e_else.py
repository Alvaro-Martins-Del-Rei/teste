#if / elif       / else
#se / se não se  / se não

entrada = input('Você quer "entrar" ou "sair" do sistema: ')

#o if e os outros são condições, ou seja, são booleans(True ou False)

if entrada == 'entrar':
    print('Você entrou no sistema!!')

elif entrada == 'sair':
    print('Você saiu dos sistema!!')

else:
    print('Você digitou nada com nada aí amigão')

print('Essa parte ta fora dos blocos de comando')
