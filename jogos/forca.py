import random


def jogar():
    print("*********************************")
    print("**boas vindas ao jogo da forca!**")
    print("*********************************")

    palavras_faceis = [
        "amor",
        "fato",
        "mito",
        "caos",
        "como",
        "esmo",
        "brio",
        "vide",
        "sede",
        "pois",
        "vida",
        "casa",
        "auge",
        "saga",
        "medo",
        "suma",
        "mote",
        "idem",
        "tolo",
        "sina",
        "urge",
        "crer",
        "pela",
        "apto",
        "zelo",
        "veio",
    ]

    palavras_medias = [
        "exceto",
        "mister",
        "vereda",
        "apogeu",
        "utopia",
        "escopo",
        "idiota",
        "casual",
        "hostil",
        "anseio",
        "legado",
        "pressa",
        "gentil",
        "alheio",
        "nocivo",
        "infame",
        "exímio",
        "adorno",
        "defina",
    ]

    palavras_dificeis = [
        "inerente",
        "respeito",
        "peculiar",
        "denegrir",
        "genocida",
        "deferido",
        "equidade",
        "pandemia",
        "iminente",
        "desgraça",
        "invasivo",
        "alienado",
        "eminente",
        "abstrato",
        "premissa",
        "conceito",
        "talarico",
        "ardiloso",
        "reiterar",
        "rapariga",
        "devaneio",
        "prodígio",
        "relativo",
        "passível",
        "conserto",
    ]

    print("qual o nivel de dificuldade voce quer?")
    print("(1)facil  (2)medio  (3)dificil ")
    dificudade = int(input("dificuldade de nivel: "))

    if dificudade == 1:
        palavra = random.choice(palavras_faceis)
        print("aqui esta a palavra", palavra)
    elif dificudade == 2:
        palavra = random.choice(palavras_medias)
        print("aqui esta a palavra", palavra)
    elif dificudade:
        palavra = random.choice(palavras_dificeis)
        print("aqui esta a palavra", palavra)
    print("fim de jogo!")


if __name__ == "__main__":
    jogar()
