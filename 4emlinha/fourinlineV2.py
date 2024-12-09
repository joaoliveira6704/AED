columns = 7
lines = 6

# Inicializa a lista com 0's. Tamanho definido anteriormente nas respectivas variáveis
gameArea = [[0 for _ in range(columns)] for _ in range(lines)]
gameOn = True

def print_game():
    """Imprime o tabuleiro do jogo."""
    global gameArea
    for i in range(len(gameArea)):
        for j in range(len(gameArea[i])):
            print(gameArea[i][j], end="  ")
        print("\n")

def check_column(player, column):
    """Tenta inserir a peça do jogador na coluna escolhida e retorna a linha."""
    for row in range(lines - 1, -1, -1):
        if gameArea[row][column] == 0:
            gameArea[row][column] = player
            return row  # Retorna a linha onde a peça foi colocada
    return -1  # Indica que a coluna está cheia

def verify_game(player, last_row, last_col):
    """Verifica se o jogador formou 4 em linha a partir da última jogada."""
    def count_consecutive(delta_row, delta_col):
        count = 0
        row, col = last_row, last_col
        while 0 <= row < lines and 0 <= col < columns and gameArea[row][col] == player:
            count += 1
            row += delta_row
            col += delta_col
        return count

    # Verificar horizontal 
    horizontal = count_consecutive(0, -1) + count_consecutive(0, 1) - 1
    if horizontal >= 4:
        return "Horizontal"

    # Verificar vertical 
    vertical = count_consecutive(-1, 0) + count_consecutive(1, 0) - 1
    if vertical >= 4:
        return "Vertical"

    # Verificar diagonal principal
    diagonal_principal = count_consecutive(-1, -1) + count_consecutive(1, 1) - 1
    if diagonal_principal >= 4:
        return "Diagonal Principal"

    # Verificar diagonal secundária 
    diagonal_secundaria = count_consecutive(-1, 1) + count_consecutive(1, -1) - 1
    if diagonal_secundaria >= 4:
        return "Diagonal Secundária"

    return None

def simulate_move(player, column):
    """Simula a jogada em uma coluna sem alterar o tabuleiro."""
    for row in range(lines - 1, -1, -1):
        if gameArea[row][column] == 0:
            return row  # Retorna a linha onde a peça seria colocada
    return -1  # Indica que a coluna está cheia

def best_move_for_computer():
    """Determina a melhor jogada para o computador."""
    for col in range(columns):
        # Tenta vencer imediatamente
        row = simulate_move(2, col)
        if row != -1:
            if verify_game(2, row, col):
                return col

    for col in range(columns):
        # Bloqueia o jogador 1 de vencer
        row = simulate_move(1, col)
        if row != -1:
            if verify_game(1, row, col):
                return col

    # Escolhe a primeira coluna válida como fallback
    for col in range(columns):
        if simulate_move(2, col) != -1:
            return col

def game():
    """Função principal para as jogadas"""
    global gameArea
    global gameOn

    nJogada = 1
    while gameOn:
        print(f"\n\nJogada {nJogada}")
        print_game()

        # Jogador 1
        print("\nJogador 1")
        try:
            player1Column = int(input(f"Escolha uma coluna (1 a {columns}): ")) - 1
        except ValueError:
            print("Deve ser um número!")
            continue

        while player1Column < 0 or player1Column >= columns:
            player1Column = int(input(f"Coluna inválida! Escolha entre 1 e {columns}: ")) - 1 

        lastRow = check_column(1, player1Column)

        while lastRow == -1:
            player1Column = int(input("Escolha outra coluna, essa está cheia: ")) - 1
            lastRow = check_column(1, player1Column)

        result = verify_game(1, lastRow, player1Column)
        if result:
            print_game()
            print(f"\nO Jogador 1 venceu com uma vitória {result} na {nJogada}ª jogada!")
            gameOn = False
            break

        print_game()

        # Jogador 2 (computador)
        print("\nJogador 2 (Computador está jogando...)")
        computerColumn = best_move_for_computer()
        lastRow = check_column(2, computerColumn)

        result = verify_game(2, lastRow, computerColumn)
        if result:
            print_game()
            print(f"\nO Computador venceu com uma vitória {result} na {nJogada}ª jogada!")
            gameOn = False
            break

        print_game()

        nJogada += 1  # Incrementa o número de jogadas

game()
