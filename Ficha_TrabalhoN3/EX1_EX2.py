def invertText(text):
    inverted = text[::-1]

    return inverted

def countText(text):
    textLen = str(len(text))
    spaces = str(text.count(" "))
    vogal_a = text.count("a")
    vogal_e = text.count("e")
    vogal_i = text.count("i")
    vogal_o = text.count("o")
    vogal_u = text.count("u")

    vogal_count = str(vogal_a + vogal_e + vogal_i + vogal_o + vogal_u)

    
    return "Tamanho do Texto: " + textLen, "Nº de Espaços: " + spaces, "Nº de Vogais: " + vogal_count

texto = input("Insira um texto: ")
inverted = invertText(texto)
counter = countText(texto)
print(inverted)
print(counter)