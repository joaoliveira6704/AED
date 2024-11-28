import os

ficheiro="ficha_trabalho8/ficheiros/dados.bin"
def escreveTexto():
    f=open(ficheiro, "wb")

    texto = input("Escreva um texto: ")

    texto1 = bytes(texto, encoding="utf-8")
    f.write(texto1)
    f.close()
    menu()

def lerTexto():
    f=open(ficheiro, "rb")

    texto = f.read()
    print(str(texto))

    f.close()
    menu()

def menu():
    print("MENU")
    print("1 - Escrever Texto")
    print("2 - Ler Texto")
    print("0 - Sair")
    opcao = input("\t\tOpção: ")
    match opcao:
        case "1":
            escreveTexto()
        case "2":
            lerTexto()
        case "0":
            exit()
        case _:
            menu()

menu()