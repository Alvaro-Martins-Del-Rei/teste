"""
Introdução ao try/except
try --> tentar executar um código
except --> ocorreu algum erro ao tentar executar
"""
numero_str = input('Vou dobrar qualquer número q vc digitar: ')

#o if não evita execessões(erros) de ocorrerem, ele apenas ta chegango a lógica em código sem execessão
#if numero_str.isdigit(): #o "is.digit" funciona assim:
                         #ele vai valer só para números inteiros, nunca para floats
                         #ele retorna valores True, então o único valor True dele é o int
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2}')
#else: 
#    print('Isso não é um número')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')

#em try/except vc consegue capturar o erro com o except
#não é muito prudente a gnt usar try/except dessa maneira
#mas nessa sessão(iniciante) vamos usar dessa maneira, pq estamos aprendendo ainda
#nas próximas sessões vamos deixar esse try/except mais bonitão
#deixar como os outros programadores mais experientes utilizam