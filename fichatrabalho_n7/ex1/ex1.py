import os

def inserirPaises():
    os.system('clear')
    
    file = open("fichatrabalho_n7/ex1/files/paises.txt", "a")

    pais = input("País: ")
    with open("fichatrabalho_n7/ex1/files/paises.txt", "r") as fileSearch:
        conteudo = fileSearch.read()
        while pais.lower() in conteudo.lower():
            print(f"\n{pais} já existe!")
            pais = input("País: ")
    continente = input("Continente: ")

    linha = pais + ";" + continente + "\n"
    file.write(linha)
    file.close()

    menu()

def consultarPaises():
    os.system('clear')
    
    file = open("fichatrabalho_n7/ex1/files/paises.txt", "r")

    print("\t País\t\tContinente")
    print("---------------------------------")
    for line in file:
        campos = line.split(";")
        print("\t", campos[0], "\t\t", campos[1].strip("\n"))

    file.close()

    menu()

def consultarContinente():
    os.system('clear')
    
    file = open("fichatrabalho_n7/ex1/files/paises.txt", "r")

    continente = input("Continente: ")

    print("\t País\t\tContinente")
    print("---------------------------------")
    for line in file:
        campos = line.split(";")
        if campos[1].strip("\n")==continente:
            print("\t", campos[0], "\t", campos[1].strip("\n"))

    file.close()

    menu()

def consultarnumeroPaises():
    os.system('clear')

    continente_count = {}

    file = open("fichatrabalho_n7/ex1/files/paises.txt", "r")

    for line in file:
        campos = line.split(";")
        continente = campos[1].strip("\n")
        if continente in continente_count:
            continente_count[continente] += 1
        else:
            continente_count[continente] = 1

    print("\tContinente\tNº de Países")
    print("---------------------------------")
    for continente, count in continente_count.items():
        print(f"\t{continente}\t\t{count}")
    
    file.close()
    
    menu()

def menu():
    print("MENU")
    print("1 - Inserir Países")
    print("2 - Consulta Países")
    print("3 - Consulta por continente")
    print("4 - Consulta nº países")
    print("0 - Sair")
    opcao = input("\t\tOpção: ")
    match opcao:
        case "1":
            inserirPaises()
        case "2":
            consultarPaises()
        case "3":
            consultarContinente()
        case "4":
            consultarnumeroPaises()
        case "0":
            exit()
        case _:
            menu()

menu()