def shortName(nome):
    pos1 = nome.find(" ")
    pos2 = nome.rfind(" ")

    pNome = nome[:pos1]
    uNome = nome[pos2:]

    nome_Curto = pNome + "" + uNome

    return nome_Curto

nomeInput = input("Nome: ")
print(shortName(nomeInput))