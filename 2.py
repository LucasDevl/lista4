import random

def adivinhar_numero():
    numero_secreto = random.randint(1, 10)
    tentativas = 3

    print("Tente adivinhar o número secreto (entre 1 e 10). Você tem 3 tentativas.")

    while tentativas > 0:
        palpite = int(input("Tentativa {}: ".format(4 - tentativas)))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto:", numero_secreto)
            return
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")

        tentativas -= 1

    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)

adivinhar_numero()
