def ordenarLista(listNum):
    """
    Sorts a list and removes duplicates
    """

    listNum.sort()

    return list(dict.fromkeys(listNum))

n = int(input("Quantos elementos deseja adicionar? "))

listNum = []

for i in range(0, n):
    num = int(input(f"Nº {i+1}: "))
    listNum.append(num)

print(ordenarLista(listNum))