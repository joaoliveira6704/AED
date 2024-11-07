import random

def biggestValue(matrix):
    """
    Gets a matrix and returns the biggest value found
    """
    maxRow = max(matrix)
    maxNumber = max(maxRow)

    print(f"Valor máximo: {maxNumber}")

    print("\n\n")
    print("     MENU      ")
    print("1 - Inicializar Matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior Valor")
    print("0 - Sair")
    option = int(input("Escolha uma das opções: "))

    match option:
        case 1:
            initMatrix(matrix=[])
        case 2:
            transposeMatrix(matrix)
        case 3:
            biggestValue(matrix)
        case _:
            print("Inválido! ")

def transposeMatrix(matrix):
    """
    Transposes a given matrix and prints it
    """
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

    for row in transposed_matrix:
        print(row)

    print("\n\n")
    print("     MENU      ")
    print("1 - Inicializar Matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior Valor")
    print("0 - Sair")
    option = int(input("Escolha uma das opções: "))

    match option:
        case 1:
            initMatrix(matrix=[])
        case 2:
            transposeMatrix(matrix)
        case 3:
            biggestValue(matrix)
        case _:
            print("Inválido! ")
    

def initMatrix(matrix):
    """
    Initializes a matrix with n dimension (n chosen by user)
    """

    dimension = int(input("Dimensão da matriz: "))

    for i in range(dimension):
        matrix.append([])
        for j in range(dimension):
            numMatrix = random.randint(10,100)
            matrix[i].append(numMatrix)
    
    print("Matriz Gerada:")
    for num in matrix:
        print(num)

    print("\n\n")
    print("     MENU      ")
    print("1 - Inicializar Matriz")
    print("2 - Matriz Transposta")
    print("3 - Maior Valor")
    print("0 - Sair")
    option = int(input("Escolha uma das opções: "))

    match option:
        case 1:
            initMatrix(matrix=[])
        case 2:
            transposeMatrix(matrix)
        case 3:
            biggestValue(matrix)
        case _:
            print("Inválido! ")


print("     MENU      ")
print("1 - Inicializar Matriz")
print("2 - Matriz Transposta")
print("3 - Maior Valor")
print("0 - Sair")
option = int(input("Escolha uma das opções: "))

matrix = []

match option:
    case 1:
        initMatrix(matrix)
    case _:
        print("Inválido! ")