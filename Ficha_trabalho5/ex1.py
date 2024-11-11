matriz = []

for i in range(3):
    matriz.append([])
    for j in range(3):
        addList = int(input(f"Linha {i+1}, coluna {j+1}: "))
        matriz[i].append(addList)

print("\n\nMatriz Original:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()

print("\n\nMatriz Transposta:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[j][i], end=" ")
    print()