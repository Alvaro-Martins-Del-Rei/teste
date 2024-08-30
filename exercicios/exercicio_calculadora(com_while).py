""" -calculadora com while - """
while True:
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    op = input('Digite um operador: (+ - / *): ')
    num_valido = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        num_valido = True
    except:
        num_valido = None

    if num_valido is None:
        print('Um ou ambos os números digitados são inválidos')
        continue

    op_permitido = '+-/*'

    if op not in op_permitido:
        print('Operador Inválido')
        continue

    if len(op) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando a sua conta. Confira o resultado abaixo: ')

    if op == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif op == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif op == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    elif op == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Deseja sair? [s] Sim: ').lower().startswith('s')
    
    if sair:
        break