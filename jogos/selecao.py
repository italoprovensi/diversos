import forca
import adivinhacao


def escolher_jogo():
    print("*********************************")
    print("*******selecione um jogo*********")
    print("*********************************")

    print("(1)forca  (2)adivinhação")
    jogo = int(input("qual jogo?:"))

    if jogo == 1:
        print("jogando forca!")
        forca.jogar()
    elif jogo == 2:
        print("jogando adivinhação")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolher_jogo()
