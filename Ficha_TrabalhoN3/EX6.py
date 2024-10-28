def standardName(nome):
    pos1 = nome.find(" ")
    pos2 = nome.rfind(" ")

    pNome = nome[:pos1]
    uNome = nome[pos2:]

    replaceString = nome.replace(" ", ";")

    spaceCount = replaceString.find(";")
    abrev = " "
    #abrev = nome[spaceCount:spaceCount+2] + "."

    for i in range(nome.find(" "), nome.rfind(" ")):
        if nome[i] == " ":
            abrev += " " + nome[i+1] + "."


    return pNome + abrev + uNome

nomeInput = input("Nome: ")
print(standardName(nomeInput))