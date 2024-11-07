import numpy as np

matriz = []

for i in range(3):
    matriz.append([])
    for j in range(3):
        addList = int(input(f"Linha {i+1}, coluna {j+1}: "))
        matriz[i].append(addList)

print("\n\nMatriz Original:")
for num in matriz:
    print(num)

print("\n\nMatriz Transposta:")
transpose= np.transpose(matriz)
for num in transpose:
    print(num)