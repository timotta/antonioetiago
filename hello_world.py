import os

def execution():
    os.system('clear')

    a = input("""

        Quer ir pra onde?

        1. Pra direita
        2. Pra esquerda

    """)

    if a == "1":
        b = input("você foi pra direita parabéns, deseja voltar? (s/n)")

        if b == "s":
            execution()

    if a == "2":
        print("Deu mole, foi pra esquerda e achou um monstro, você morreu")


execution()