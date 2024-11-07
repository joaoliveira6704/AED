estacionamento = [[0 for _ in range(5)] for _ in range(3)]

def estadoParque():
    lugarLivre = 0
    lugarOcupado = 0
    if len(estacionamento) == 0:
        print("\nParque Vazio!\n\n")
    else:
        for i in range(3):
            for j in range(5):
                if estacionamento[i][j] == 0:
                    lugarLivre += 1
                else:
                    lugarOcupado += 1
    
    print(f"\n\nLugares Ocupados: {lugarOcupado}\nLugares Livres: {lugarLivre}\n\n")

def entradaVeiculo():
    for i in range(3):
        for j in range(5):
            if estacionamento[i][j] == 0:
                estacionamento[i][j] = 1
                print(f"\n\nEstacionado! - Fila {i+1}, Lugar {j+1}\n\n")
                return
    print("Parque completo!")

def saidaCarro():
    if len(estacionamento) == 0:
        print("\n\nEstacionamento Vazio! Impossível remover carros!\n\n")
    else:
        filaPos = int(input("Indique a fila do carro a remover: "))
        while filaPos < 1 or filaPos > 3:
            filaPos = int(input("Indique a fila do carro a remover (entre 0 e 3): "))

        lugarPos = int(input("Indique o lugar do carro a remover: "))
        while lugarPos < 1 or lugarPos > 5:
            lugarPos = int(input("Indique o lugar do carro a remover (entre 0 e 5): "))
    
    estacionamento[filaPos-1][lugarPos-1] = 0

    print("Carro removido com sucesso!")
    
def menu():
    print("-----MENU-----")
    print("1 - Entrada de Veículo")
    print("2 - Saída de carro")
    print("3 - Estado do Parque")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        opcao = int(input("Opção Inválida! Escolha uma opção: "))
    except:
        opcao = int(input("Erro desconhecido! Escolha uma opção: "))
    else:
        match opcao:
            case 1:
                entradaVeiculo()
            case 2:
                saidaCarro()
            case 3:
                estadoParque()
            case 0:
                exit()
            case _:
                print("Inválido!")

while True:
    menu()