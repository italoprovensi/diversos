import random


def jogar():
    print("*********************************")
    print("**boas vindas ao jogo da forca!**")
    print("*********************************")

    palavra = 'arnold schwarzenegger'
    letras_acertadas = ''
    tentativas = 0
    while True:

        chute = input('digite uma letra ')
        tentativas += 1

        if len(chute) > 1:
            print('digite apenas uma letra')
            print('suas tentativas ', tentativas)
            continue

        if chute in palavra:
            letras_acertadas += chute

        palavra_formada = ''
        for letras_secreta in palavra:
            if letras_secreta in letras_acertadas:
                palavra_formada += letras_secreta
            else:
                palavra_formada += '*'

        print(palavra_formada)
        if palavra_formada == palavra:
            print('voce acertou ')
            break

        print('suas tentativas ', tentativas)

    aa = 1


if __name__ == "__main__":
    jogar()
