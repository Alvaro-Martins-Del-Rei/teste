#Operador Lógico
#and(e) or(ou) not(não)
#and - todas as condições precisam ser verdadeiras
#se qualquer valor for considerado falso,
#a expressão inteira será avaliada naquela valor
#são considerados falsy (que vc já viu)
#0, 0.0, '', False
#também existe o tipo none que é
#usado para representar um não valor - basicamente só aparece pra falar "pode ficar tranquilo q eu não existo cachorro"

#um programa bem porco pra mostrar como q funciona o "and" +/-

print('O código abaixo faz parte do operador and:\n')

entrada = input('[E] Entrar    [S] Sair: ')
senha_d = input('Digite a senha: ')

senha_p = '123456'

if entrada == 'E' and senha_d == senha_p:
    print('\nVocê entrou no sistema\n')
else:
    print('\nVocê saiu do sistema\n\n')

#or - qualquer condição verdadeira avalia
#toda a expressão como verdadeira.
#se qualquer valor for considerado verdadeiro,
#a expressão inteira será avaliada naquele valor.
#são considerados falsy (que vc já viu)
#0, 0.0, '', False
    
print('Esse código já faz parte do operador or:\n')

entrada = input('[E] Entrar    [S] Sair: ')
senha_d = input('Digite a senha: ')

senha_p = '123456'

if (entrada == 'E' or entrada == 'e') and senha_d == senha_p:
    print('\nVocê entrou no sistema\n')
else:
    print('\nVocê saiu do sistema\n\n')