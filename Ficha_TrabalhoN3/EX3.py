def capicua(text):
    firstpart = text[:int(len(text)/2)]
    secondpart = text[int(len(text)/2):]
    secondpart_Invert = secondpart[::-1]

    if firstpart == secondpart_Invert:
        True
        capic = f"{text} é uma capicua"
    else:
        False
        capic = f"{text} não é uma capicua"
    
    return capic
    

palavra = input("Escreva uma palavra: ")

capicuaFind = capicua(palavra)
print(capicuaFind)