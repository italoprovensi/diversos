class Calculadora:
    def __init__(self, numero1, numero2, operacao):
        self.numero1 = numero1
        self.numero2 = numero2
        self.operacao = operacao

    def verifica_operacao(self):
        if self.operacao == "soma":
            print(self.numero1 + self.numero2)
        elif self.operacao == "subtrair":
            print(self.numero1 - self.numero2)
        elif self.operacao == "multiplicar":
            print(self.numero1 * self.numero2)
        elif self.operacao == "dividir":
            print(self.numero1 / self.numero2)
        else:
            print("digite uma operação valida: ")


while True:
    conta = Calculadora(int(input("primeiro numero:")), int(input("segundo numero:")), input("digite uma operação: "))
    conta.verifica_operacao()

    continuar = input("deseja continuar? (S/N)")

    if continuar != "S":
        break
