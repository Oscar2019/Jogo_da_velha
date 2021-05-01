import time
import random
import math

def altera_matriz(mat: list, x: int, y: int, val: str):
    """
        Essa função altera um elemetno da matriz
    """
    mat[x][y] = val

def print_matriz(mat: list):
    """
        Essa função printa uma matriz
    """
    for p in mat:
        print(f"{p[0]} {p[1]} {p[2]}")

def create_matriz():
    """
        Essa função cria uma matriz para colocar os resultados
    """
    return [[" " for _ in range(3)] for _ in range(3)]

def create_jogador(nome, simbolo):
    """
        Cria uma tupla com o nome e o símbolo
    """
    return (nome, simbolo)

def pessoa_joga(mat: list, jogador):
    """
        Cuida da jogada do jogador
    """
    print_matriz(mat)
    nome, simbolo = jogador
    x, y = map(int, input(f"Onde o {nome} deseja jogar o {simbolo}? ").split())
    altera_matriz(mat, x, y, simbolo)

def venceu(mat: list):
    """
        Decide se alguém venceu a partida
    """
    if mat[0][1] != ' ' and mat[0][0] == mat[0][1] and mat[0][1] == mat[0][2]:
        return True
    elif mat[1][1] != ' ' and mat[1][0] == mat[1][1] and mat[1][1] == mat[1][2]:
        return True
    elif mat[2][1] != ' ' and mat[2][0] == mat[2][1] and mat[2][1] == mat[2][2]:
        return True
    elif mat[1][0] != ' ' and mat[0][0] == mat[1][0] and mat[1][0] == mat[2][0]:
        return True
    elif mat[1][1] != ' ' and mat[0][1] == mat[1][1] and mat[1][1] == mat[2][1]:
        return True
    elif mat[1][2] != ' ' and mat[0][2] == mat[1][2] and mat[1][2] == mat[2][2]:
        return True
    elif mat[1][1] != ' ' and mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2]:
        return True
    elif mat[1][1] != ' ' and mat[2][0] == mat[1][1] and mat[1][1] == mat[0][2]:
        return True
    return None

def tem_jogadas(mat: list):
    """
        Verifica se existe jogadas diponíveis
    """
    for p in mat:
        for q in p:
            if q == ' ':
                return True
    return False

def melhor_possibilidade(mat: list, simbolos: list, pesos: list, vez: int, auz: int = 0):
    qtd = 0
    maior = -1
    pos = (0, 0)
    for i in range(3):
        linha = mat[i]
        for j in range(3):
            if linha[j] == ' ':
                if maior == -1:
                    (i, j)
                linha[j] = simbolos[vez]
                if venceu(mat):
                    qtd += pesos[vez]
                    if maior < pesos[vez]:
                        maior = pesos[vez]
                        pos = (i, j)
                elif not tem_jogadas(mat):
                    qtd += pesos[2]
                    if maior < pesos[2]:
                        maior = pesos[2]
                        pos = (i, j)
                else:
                    nqtd, npos = melhor_possibilidade(mat, simbolos, pesos, vez ^ 1, auz + 1)
                    if maior < nqtd:
                        maior = nqtd
                        pos = (i, j)
                    qtd += nqtd
                linha[j] = ' '
    return (qtd, pos)

def computador_joga(mat: list, jogador):
    """
        Cuida da jogada do jogador
    """
    print_matriz(mat)
    nome, simbolo = jogador
    simbolos = None
    pesos = [1, 0, 0]
    if simbolo == "X":
        simbolos = ["X", "O"]
    else:
        simbolos = ["O", "X"]
    _, pos = melhor_possibilidade(mat, simbolos, pesos, 0)
    x, y = pos
    altera_matriz(mat, x, y, simbolo)


def main():
    while True:
        num_jogadores = int(input("Deseja jogar com 1 ou 2 player? "))
        
        jogadores = [None, None]
        if num_jogadores == 1:
            jogadores = [pessoa_joga, computador_joga]
        else:
            jogadores = [pessoa_joga, pessoa_joga]

        random.seed(math.trunc(time.time()))
        simbolos = None
        nomes = ["player 1", "player 2"]
        player1 = None
        player2 = None
        players = None
        player_atual = random.randint(0, 1)
        if player_atual == 0: # X sempre começa
            simbolos = ["X", "O"]
            player1 = create_jogador("player 1", "X")
            player2 = create_jogador("player 2", "O")
        else:
            simbolos = ["O", "X"]
            # player1 = create_jogador("player 2", "X")
            # player2 = create_jogador("player 1", "O")
            player1 = create_jogador("player 1", "O")
            player2 = create_jogador("player 2", "X")
        players = [player1, player2]
        player_atual ^= 1
        
        mat = create_matriz()

        while tem_jogadas(mat) and not venceu(mat):
            player_atual ^= 1
            print(player_atual, jogadores[player_atual].__name__)
            jogadores[player_atual](mat, players[player_atual])
        
        print_matriz(mat)
        if venceu(mat):
            print(f"O {nomes[player_atual]} venceu")
        else:
            print(f"Deu velha")

        res = input("Deseja jogar novamente?('S' ou 'N') ")
        if res == 'N':
            break

if __name__ == "__main__":
    main()