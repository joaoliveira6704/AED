def removeSpaces(text):

    while text.find("  ") != 1:
        text = text.replace("  ", " ")
    
    return text


texto = input("Escreva um texto: ")
print(removeSpaces(texto))