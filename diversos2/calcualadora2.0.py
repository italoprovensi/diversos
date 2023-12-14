while True:

    numero1 = input('digite o primeiro numero ')
    numero2 = input('digite o segundo numero ')
    operador = input('digite um operador [+-/*] ')
    numero_valido = None

    nu_1_float = 0
    nu_2_float = 0

    try:
        nu_1_float = float(numero1)
        nu_2_float = float(numero2)
        numero_valido = True

    except Exception as error:
        print(error)
        numero_valido = None

    if numero_valido is None:
        print("algum numero foi invalido , tente novamente")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("operador invalido")
        continue

    if len(operador) > 1:
        print('apenas 1 operador')

    if operador == '+':
        print(f'primeiro numero', nu_1_float, 'segundo numero', nu_2_float, 'resultado', nu_1_float + nu_2_float)
    elif operador == '-':
        print('primeiro numero',nu_1_float , 'segundo numero', nu_2_float, 'resultado', nu_1_float - nu_2_float)
    elif operador == '/':
        print('primeiro numero', nu_1_float, 'segundo numero', nu_2_float, 'resultado', nu_1_float / nu_2_float)
    elif operador == '*':
        print('primeiro numero', nu_1_float, 'segundo numero', nu_2_float, 'resultado', nu_1_float * nu_2_float)

    sair = input("sair? [s]im ou [n]ão ").lower().startswith('s')
    if sair is True:
        break
