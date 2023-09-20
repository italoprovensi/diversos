def jogar():
    import random

    print("*********************************")
    print("boas vindas ao jogo de advinhação")
    print("*********************************")

    numero_secreto = round(random.randrange(0, 101))
    total_de_tentativas = 0

    print("qual o nivel de dificuldade voce quer?")
    print("(1)facil  (2)medio  (3)dificil ")
    nivel = int(input("dificuldade de nivel: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa {} de {} ".format(rodada, total_de_tentativas))
        chute_str = input("digite o seu numero entre 1 a 100: ")
        print("voce digitou", chute_str)

        chute = int(chute_str)
        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if chute < 1 or chute > 100:
            print("voce deve digitar um numero entre 1 a 100!")
            continue
        if acertou:
            print("voce acertou!")
            break
        else:
            if maior:
                print("voce errou! o seu numero foi maior ! ")
            elif menor:
                print("voce errou! o seu numero foi menor!")

    print("fim de jogo")


if __name__ == "__main__":
    jogar()
