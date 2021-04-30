import time
import random
import math

def altera_matriz(mat: list, x: int, y: int, val: str):
    mat[x][y] = val

def print_matriz(mat: list):
    for p in mat:
        print(f"{p[0]} {p[1]} {p[2]}")

def create_matriz():
    return [[" " for _ in range(3)] for _ in range(3)]

def create_jogador(nome, simbolo):
    return (nome, simbolo)

def pessoa_joga(mat: list, jogador):
    print_matriz(mat)
    nome, simbolo = jogador
    x, y = map(int, input(f"Onde o {nome} deseja jogar o {simbolo}? ").split())
    altera_matriz(mat, x, y, simbolo)

def venceu(mat: list):
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
    for p in mat:
        for q in p:
            if q == ' ':
                return True
    return False

def main():
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
        pessoa_joga(mat, players[player_atual])
    
    print_matriz(mat)
    if venceu(mat):
        print(f"O {nomes[player_atual]} venceu")
    else:
        print(f"Deu velha")


if __name__ == "__main__":
    main()