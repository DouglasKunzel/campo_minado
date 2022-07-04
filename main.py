import random


def gerar_tabuleiro():
    tabuleiro = [["*" for lin in range(10)] for col in range(10)]
    return tabuleiro


def gerar_bombas():
    bombas = gerar_tabuleiro()
    quantidade = 10
    while quantidade > 0:
        rand_lin = random.randint(0, 9)
        rand_col = random.randint(0, 9)
        if bombas[rand_lin][rand_col] == "*":
            bombas[rand_lin][rand_col] = "X"
            quantidade -= 1
    return bombas


def imprimir_tabuleiro(tabuleiro):
    print("\n\n\t\t| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |")
    col = 0
    lin = 0
    for lin in range(10):
        for col in range(10):
            if col == 0:
                print("      ", end="")
                print(lin, "|", end="")
                print("", end="")
            print(" {} ".format(tabuleiro[lin][col]), end="")
            print("|", end="")
            print("", end="")
        print("\n", end="")
    print("\n")


def valida_jogada(lin, col, tabuleiro, tabuleiro2, var):
    if tabuleiro[lin][col] == "*":
        contagem = valida_bomba2(lin, col, tabuleiro2)
        tabuleiro[lin][col] = contagem
        if contagem == 0:
            for x in range(max(0, lin - 1), min(10, lin + 2)):
                for y in range(max(0, col - 1), min(10, col + 2)):
                    if x != lin or y != col:
                        tabuleiro = valida_jogada(x, y, tabuleiro, tabuleiro2, 1)
        elif contagem == "X":
            print("VOCE PERDEU!!!")
            return 3
    else:
        if var == 0:
            print("\t---Local ja jogado, Jogue novamente---\n\n")

    return tabuleiro


def jogada(tabuleiro, tabuleiro2):
    lin = int(input("Digite qual linha deseja jogar: "))
    col = int(input("Digite qual coluna deseja jogar: "))
    jogada = valida_jogada(lin, col, tabuleiro, tabuleiro2, 0)
    imprimir_tabuleiro(tabuleiro)
    if checagem_vitoria(tabuleiro) == 1:
        return 1
    if jogada == 3:
        return 1
    return 0


def valida_bomba2(lin, col, bombas):
    contagem = 0
    if bombas[lin][col] == "X":
        print("KABUUUUUUUUUUMMMM")
        return "X"

    for x in range(max(0, lin - 1), min(10, lin + 2)):
        for y in range(max(0, col - 1), min(10, col + 2)):
            if bombas[x][y] == "X":
                contagem += 1

    return contagem


def checagem_vitoria(bombas):
    numbombas = 10
    contagem = 0
    for x in range(10):
        for y in range(10):
            if bombas[x][y] == "*":
                contagem += 1
    if contagem == numbombas:
        print("VOCE GANHOU PARABENS!!!!")
        return 1
    return 0


def jogo(tabuleiro, tabuleiro2):
    y = 1
    while y == 1:
        x = 0
        imprimir_tabuleiro(tabuleiro)
        while x == 0:
            x = jogada(tabuleiro, tabuleiro2)
        y = int(input("\n\tDigite 1 para jogar novamente.\n\tDigite 2 para parar de jogar."))


tabuleiro2 = gerar_bombas()
tabuleiro = gerar_tabuleiro()
jogo(tabuleiro, tabuleiro2)
print("FIM DE JOGO")
