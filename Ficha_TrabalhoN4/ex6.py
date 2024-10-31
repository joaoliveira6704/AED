def searchNumber(lista, pesquisa):
    """
    Returns the positions of a value in a list
    """
    listPos = []

    for index, num in enumerate(lista):
        if num == pesquisa:
            listPos.append(index)
    
    if len(listPos) >= 1:
        return f"Posições com o valor {pesquisa}: {listPos}"
    else:
        return f"Não foi encontrado nenhum número na lista com o valor {pesquisa}"

listNum = []

for i in range(10):
    num = int(input(f"Nº {i+1}: "))
    listNum.append(num)

numPesquisa = int(input("Introduza o número a pesquisar: "))

print(searchNumber(listNum, numPesquisa))
