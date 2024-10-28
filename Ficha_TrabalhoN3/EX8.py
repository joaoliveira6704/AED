def reverseWords(text):
    """
    Recebe um texto e devolve o mesmo texto, com palavras em ordem inversa.
    """
    replaced = text.replace(" ", ";")
    
    splitedList = replaced.split(";")

    reverse = list(reversed(splitedList))

    for i in reverse:
        print(i, end=" ")


texto = input("Insira um texto: ")
reverseWords(texto)