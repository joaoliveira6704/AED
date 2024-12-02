columns=7
lines=6

#Inicializa a lista com 0's. Tamanho definido anteriormente nas respetivas variáveis
gameArea = [[0 for i in range(columns)] for i in range(lines)]

def printGame():
    global gameArea

    for line in gameArea:
        print(line)


def game():
    global gameArea

    nJogada = 1

    print(f"Jogada {nJogada}")
    print("Jogador 1")
    try:
        player1Column = int(input("Coluna: "))
        raise ValueError
    except ValueError:
        print("deve ser um número!")

    while player1Column>columns:
        player1Column = int(input("Coluna: "))

    while gameArea[lines-1][player1Column-1] == 1:
        print("Já fez essa jogada, tente novamente!")
        print("Jogador 1")
        player1Column = int(input("Coluna: "))
        printGame()
        
    while gameArea[lines-1][player1Column-1] == 2:
        print("O jogador 2 já fez essa jogada, tente novamente!")
        print("Jogador 1")
        player1Column = int(input("Coluna: "))
        printGame()

    if gameArea[lines-1][player1Column-1] == 0:
        gameArea[lines-1][player1Column-1] = 1

    printGame()

    print("Jogador 2")
    player2Column = int(input("Coluna: "))

    while gameArea[lines-1][player2Column-1] == 1:
        print("O jogador 1 já fez essa jogada, tente novamente!")
        print("Jogador 2")
        player2Column = int(input("Coluna: "))
        printGame()

    while gameArea[lines-1][player2Column-1] == 2:
        print("Já fez essa jogada, tente novamente!")
        print("Jogador 2")
        player2Column = int(input("Coluna: "))
        printGame()

    if gameArea[lines-1][player2Column-1] == 0:
        gameArea[lines-1][player2Column-1] = 2
    
    print("\n\n")
    printGame()

    game()

game()