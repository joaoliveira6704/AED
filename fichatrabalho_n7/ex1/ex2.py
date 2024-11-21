import os
from datetime import datetime
import time

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

def consultarData():
    os.system('clear')
    
    file = open("fichatrabalho_n7/ex1/files/temperatura.txt", "r")
    
    dataConsulta = input("Data da Consulta: ")

    print("Data\t\t Hora\t\tTemperatura")
    print("---------------------------------------------")
    for line in file:
        campos = line.split(";")
        if campos[0]==dataConsulta:
            print(campos[0], "\t", campos[1], "\t", campos[2])

    file.close()

    menu()

def consultarEstatistica():
    os.system('clear')
    temperaturas = []
    
    file = open("fichatrabalho_n7/ex1/files/temperatura.txt", "r")

    for line in file:
        campos = line.split(";")
        temperaturas.append(int(campos[2].strip("\n")))

    valorMax = max(temperaturas)
    valorMin = min(temperaturas)
    media = sum(temperaturas)/len(temperaturas)
    
    print(f"O maior valor de temperatura registada for de {valorMax}\n")
    print(f"O menor valor de temperatura registada for de {valorMin}\n")
    print(f"O valor médio de temperatura registada for de {media:.2f}\n")

    file.close()

    menu()

def menu():
    print("MENU")
    print("1 - Consulta por data")
    print("2 - Consulta Estatística")
    print("0 - Sair")
    opcao = input("\t\tOpção: ")
    match opcao:
        case "1":
            consultarData()
        case "2":
            consultarEstatistica()
        case "0":
            exit()
        case _:
            menu()

menu()