class Login:
    def __init__(self, conta, senha):
        self.conta = conta
        self.senha = senha


pessoa1 = Login("joao", "12345")
pessoa2 = Login("maria", "33333")
pessoa3 = Login("igor", "11111")
pessoa4 = Login("andreia", "22222")
pessoa5 = Login("leandro", "44444")

conta = input("conta: ")
senha = input("senha: ")

if conta == pessoa1.conta and senha == pessoa1.senha:
    print("bem vindo, joao!")
elif conta == pessoa2.conta and senha == pessoa2.senha:
    print("bem vindo, maria!")
elif conta == pessoa3.conta and senha == pessoa3.senha:
    print("bem vindo, igor!")
elif conta == pessoa4.conta and senha == pessoa4.senha:
    print("bem vindo, andreia!")
elif conta == pessoa5.conta and senha == pessoa5.senha:
    print("bem vindo, leandro!")
else:
    print("conta ou senha invalida! tente novamente")
