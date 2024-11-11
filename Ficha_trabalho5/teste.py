matrix = []

nLinhas = int(input("Número de linhas: "))
nColunas = int(input("Número de colunas: "))

for i in range(nLinhas):
    matrix.append([])
    for j in range(nColunas):
        matrix[i].append(int(input(f"Linha {i+1}, Coluna {j+1}: ")))

print("\n\nMatriz normal:")
for i in range(nLinhas):
    for j in range(nColunas):
        print(matrix[i][j],end=" ")
    print()

print("\n\nMatriz transposta:")
for i in range(nColunas):
    for j in range(nLinhas):
        print(matrix[j][i],end=" ")
    print()