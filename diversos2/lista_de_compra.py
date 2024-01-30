lista = []

while True:
    escolha = input('[i]nserir , [a]pagar , [v]er a lista: ')
    escolha_minuscola = escolha.lower()
    try:
        if escolha_minuscola == 'i':
            add = str(input('adicionar oq? '))
            lista.append(add)

        elif escolha_minuscola == 'a':
            try:
                apagar = input('apagar qual item? "coloque o nome."')
                lista.remove(apagar)
            except Exception as erro:
                print(erro)
                print('nao foi possível apagar esse item, verifique se ele exite.')
        elif escolha_minuscola == 'v':
            for numero, item in enumerate(lista):
                print(numero, item)

        else:
            print('digite algo valido.')

    except Exception as erro:
        print(erro)
        print('deu ruim.')
