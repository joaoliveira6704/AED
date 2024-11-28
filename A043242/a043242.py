#Número: A043242
#Nome: João Oliveira
#NOTA: MacOS, o os.system("clear") não deve funcionar no windows.
import os

def consultaDistancia():
    """Permite consultar as Datas e Tempos Registados para cada distância"""
    os.system("clear")

    #Abre o ficheiro em modo leitura
    ficheiro = open("atividades.txt", "r")

    consulta = input("Consulta de: ")

    #Verifica se a consulta é feita com os valores (5k, 10k ou 21k)
    while consulta != "5k" and consulta != "10k" and consulta != "21k":
        os.system("clear")
        consulta = input("Erro! Valores devem ser (5k, 10k, 21k)!\n\nConsulta de:")
    
    print("\t   Data\t\tTempo Registado")
    print("\t------------------------------------------")

    #Mostra a data e o tempo registado por cada linha
    for line in ficheiro:
        campos = line.split(";")
        if consulta == campos[1]:
            print(f"\t{campos[0]}\t{campos[2].strip("\n")}")
    
    #Fecha o ficheiro e espera por interação do utilizador para voltar ao menu
    ficheiro.close()
    input()

def melhoresTempos():
    """Mostra os melhores tempos para cada distância"""
    os.system("clear")

    #Abre o ficheiro em modo leitura
    ficheiro = open("atividades.txt", "r")

    #Listas para guardar tempos por cada k: 5k, 10k ou 21k
    tempo5k = []
    tempo10k = []
    tempo21k = []

    #Percorre cada linha do ficheiro e adiciona os tempos correspondentes à linha onde a distância é igual a 5k, 10k ou 21k
    for line in ficheiro:
        campos = line.split(";")
        if campos[1] == "5k":
            tempo5k.append(float(campos[2].strip("\n")))
        elif campos[1] == "10k":
            tempo10k.append(float(campos[2].strip("\n")))
        elif campos[1] == "21k":
            tempo21k.append(float(campos[2].strip("\n")))

    #Guarda numa variável o tempo mais baixo encontrado (melhor tempo), para cada k (5k,10k,21k)
    melhorTempo5k = min(tempo5k)
    melhorTempo10k = min(tempo10k)
    melhorTempo21k = min(tempo21k)

    data5k =""
    data10k =""
    data21k =""

    #Volta a percorrer o ficheiro "atividades.txt", compara os tempos e adiciona a data
    ficheiro2 = open("atividades.txt", "r")
    for line in ficheiro2:
        campos = line.split(";")
        tempo = float(campos[2].strip("\n"))
        if tempo == melhorTempo5k and campos[1] == "5k":
            data5k += campos[0] + ","
        elif tempo == melhorTempo10k and campos[1] == "10k":
            data10k += campos[0] + ","
        elif tempo == melhorTempo21k and campos[1] == "21k":
            data21k += campos[0] + ","

    print("\t\t  Tempo\t  Data")
    print("-----------------------------------------------------")
    print(f"Melhor tempo 5K:  {melhorTempo5k} - {data5k.strip(",")}\nMelhor Tempo 10K: {melhorTempo10k}  - {data10k.strip(",")}\nMelhor Tempo 21K: {melhorTempo5k} - {data21k.strip(",")}")
    ficheiro.close()
    ficheiro2.close()

    input()

def progressoPessoal():
    """Guarda a distância percorrida pelo utilizador em cada mês do ano"""

    #Cria a pasta, caso não exista
    if not os.path.exists("ficheiros"):
        os.mkdir("ficheiros")

    f = open("ficheiros/progresso.txt", "w")

    meses=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    #Percorre os meses e pede o valor percorrido pelo utilizador, adiciona à lista
    for mes in meses:
        valorPercorrido = int(input(f"Valor Percorrido no mês de {mes}: "))
        f.writelines(f"{mes};{valorPercorrido}\n")

    print("Progresso.txt Criado com sucesso!")

    f.close()
    input()

#Correr sempre o menu
while True:
    os.system("clear")
    print("Menu")
    print("1 - Consulta por Distância")
    print("2 - Consulta Melhores Tempos")
    print("3 - Gravar Progresso")
    print("0 - Sair")
    op = input("\n\tOpção: ")
    #verifica que a opção escolhida é válida, se não for volta a pedir.
    match op:
        case "1":
            consultaDistancia()
        case "2":
            melhoresTempos()
        case "3":
            progressoPessoal()
        case "0":
            exit()
        case _:
            print("Opção não encontrada, tente novamente.")
            input()
