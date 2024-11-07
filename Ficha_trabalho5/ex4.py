def somarMatrizes():
    matriz1 = []
    matriz2 = []
    matrizSoma = []

    numLinhas = int(input("\n\nNúmero de Linhas: "))
    numColunas = int(input("Número de Colunas: "))

    print("\nMatriz 1:")
    for i in range(numLinhas):
        matriz1.append([])
        matrizSoma.append([])
        for j in range(numColunas):
            matriz1[i].append(int(input(f"Linha {i+1}, Coluna {j+1}: ")))
            matrizSoma[i].append(0)
    
    print("\nMatriz 2:")
    for i in range(numLinhas):
        matriz2.append([])
        for j in range(numColunas):
            matriz2[i].append(int(input(f"Linha {i+1}, Coluna {j+1}: ")))

    for i in range(numLinhas):
        for j in range(numColunas):
            matrizSoma[i][j] = matriz1[i][j] + matriz2[i][j]
    
    print("\n\nMatriz 1:\tMatriz 2:\tResultado:")
    for i in range(len(matriz1)):
        linha_matriz1 = " ".join(str(x) for x in matriz1[i])
        linha_matriz2 = " ".join(str(x) for x in matriz2[i])
        linha_resultado = " ".join(str(x) for x in matrizSoma[i])
        
        print(f"{linha_matriz1}\t\t{linha_matriz2}\t\t{linha_resultado}")

def subtrairMatrizes():
    matriz1 = []
    matriz2 = []
    matrizSoma = []
    
    numLinhas = int(input("\n\nNúmero de Linhas: "))
    numColunas = int(input("Número de Colunas: "))

    print("\nMatriz 1:")
    for i in range(numLinhas):
        matriz1.append([])
        matrizSoma.append([])
        for j in range(numColunas):
            matriz1[i].append(int(input(f"Linha {i+1}, Coluna {j+1}: ")))
            matrizSoma[i].append(0)
    
    print("\nMatriz 2:")
    for i in range(numLinhas):
        matriz2.append([])
        for j in range(numColunas):
            matriz2[i].append(int(input(f"Linha {i+1}, Coluna {j+1}: ")))

    for i in range(numLinhas):
        for j in range(numColunas):
            matrizSoma[i][j] = matriz1[i][j] - matriz2[i][j]
    
    print("\n\nMatriz 1:\tMatriz 2:\tResultado:")
    for i in range(len(matriz1)):
        linha_matriz1 = " ".join(str(x) for x in matriz1[i])
        linha_matriz2 = " ".join(str(x) for x in matriz2[i])
        linha_resultado = " ".join(str(x) for x in matrizSoma[i])
        
        print(f"{linha_matriz1}\t\t{linha_matriz2}\t\t{linha_resultado}")

def menu():
    print("-----MENU-----")
    print("1 - Somar Matrizes")
    print("2 - Subtrair Matrizes")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        opcao = int(input("Opção Inválida! Escolha uma opção: "))
    except:
        opcao = int(input("Erro desconhecido! Escolha uma opção: "))
    else:
        match opcao:
            case 1:
                somarMatrizes()
            case 2:
                subtrairMatrizes()
            case 0:
                exit()
            case _:
                print("Inválido!")

while True:
    menu()