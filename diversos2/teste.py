def minha_funcao():
    try:
        idade = 20

        if idade < 10:
            print('x')
        else:
            idade[0] = 29
            print(idade)

    except Exception as error:
        print('deu erro pq o banco ta fora do ar', error)


minha_funcao()