def tirarticket(fila):
    pos = fila.index(0)

    if pos < 20:
        fila.insert(pos, 1)
        filaDuplicate.append(pos+1)
        msg = f"Ticket tirado com sucesso com o número {pos+1}!"
    else:
        msg = "Fila cheia!"
    
    return msg

def atendimento(fila):
    exists = fila.count(1)

    if exists >= 1:
        pos = fila.index(1)
        numeroSenha = filaDuplicate[pos]

        fila.pop(pos)
        filaDuplicate.pop(pos)

        fila.append(0)

        msg = f"Senha nº {numeroSenha} atendida!"
    else:
        msg = f"Não existem senhas para ser atendidas de momento!"
        
    return msg

def estadofila(fila):
    lugaresOcupados = 0

    for valor in fila:
        if valor == 1:
            lugaresOcupados += 1
    
    lugaresLivres = 20 - lugaresOcupados

    return f"{lugaresOcupados} lugares ocupados. {lugaresLivres} Lugares livres."


def menu():
    print("    MENU")
    print("1 - Tirar Ticket")
    print("2 - Atendimento")
    print("3 - Estado da fila de espera")
    print("0 - Sair")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao > 3:
                raise IndexError
        except IndexError:
            print("Opção inexistente!!")
        except ValueError:
            print("A opção inserida deve ser um número!")
        else:
            match opcao:
                case 0:
                    exit()
                case 1:
                    print(tirarticket(fila))
                case 2:
                    print(atendimento(fila))
                case 3:
                    print(estadofila(fila))

fila = [0 for i in range(20)]
filaDuplicate = []

while True:
    menu()