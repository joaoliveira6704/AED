def nivel1():
    tempC = float(input("Temperatura em ºcelsius:"))
    tempF = (1.8 * tempC) + 32

    print("Temperatura em ºFahreneit {:.2f}".format(tempF))

def nivel2():
    pNome = input("Nome próprio: ")
    apelido = input("Apelido: ")

    print("\n {}, {}".format(apelido, pNome))

def nivel3():
    altura = float(input("Insira a sua altura(cm): "))

    pIdeal = (altura-100) * 0.9 

    print("Peso Ideal: {:.1f}".format(pIdeal))
    
def nivel4():
    peso = float(input("Insira o seu peso(kg): "))
    altura = float(input("Insira a sua altura(m): "))
    imc = peso/(altura**2)

    print("O seu imc é {:.2f}".format(imc))
    
def nivel5():
    segundos = int(input("Indique o tempo em segundos: "))
    horas = segundos/3600
    print(str(horas))
    minutos = (horas - int(horas)) * 60
    segundos = (minutos - int(minutos)) * 60
    
    print("{:.0f} horas, {} minutos, {:.0f} segundos".format(horas, int(minutos), segundos))

def nivel6():
    num = int(input("Indique um número inteiro: "))

    if num % 2 == 0:
        print("O número {} é par".format(num))
    else:
        print("O número {} é ímpar".format(num))

def nivel7():
    sexo = input("Indique o Sexo(M/F): ")
    idade = int(input("Indique a idade: "))

    match sexo.lower(): 
        case "m":
            fcm = 220 - idade
            print("FCM = {} bpm".format(fcm))
        case "f":
            fcm = 226 - idade
            print("FCM = {} bpm".format(fcm))
        case _:
            print("Inválido")

def nivel8():
    sexo = input("Indique o Sexo(M/F): ")
    altura = int(input("Indique a Altura(cm): "))

    match sexo.lower():
        case "m":
            k = 4
            pesoIdeal = ((altura-100) - (altura-150))/k
        case "f":
            k = 2
            pesoIdeal = ((altura-100) - (altura-150))/k
        case _:
            print("Inválido")

    print("O peso ideal é {:.2f} kg".format(pesoIdeal))

def nivel9():
    peso = float(input("Insira o seu peso(kg): "))
    altura = float(input("Insira a sua altura(m): "))
    imc = peso/(altura**2)

    if imc < 18.5:
        tipoPeso = "Baixo Peso"
    elif imc >= 18.5 and imc <= 24.9:
        tipoPeso = "Peso Normal"
    elif imc >= 25 and imc <= 29.9:
        tipoPeso = "Peso Normal"
    elif imc >= 30 and imc <= 34.9:
        tipoPeso = "Peso Normal"
    elif imc >= 35 and imc <= 39.9:
        tipoPeso = "Peso Normal"
    elif imc > 40:
        tipoPeso = "Peso Normal"

    print("O seu imc é {:.2f}\n\t {}".format(imc, tipoPeso))

def nivel10():
    print("\t\t1 - Mercúrio\n\t\t2 - Venus\n\t\t3 - Marte\n\t\t4 - Júpiter\n\t\t5 - Saturno\n\t\t6 - Urano\n\t\t7 - Neptuno")

    pesoTerra = int(input("Indique o seu peso (kg): "))
    codPlaneta = int(input("Indique o Código do planeta: "))

    match codPlaneta:
        case 1 | 3:
            gravidade = 0.37
        case 2:
            gravidade = 0.9
        case 4:
            gravidade = 2.53
        case 5:
            gravidade = 1.06
        case 6:
            gravidade = 0.91
        case 7:
            gravidade = 1.14
        case _:
            print("Código Inválido")

    pesoPlaneta = (pesoTerra * gravidade) / 0.98
    print("O seu peso de {:.2f}kg no planeta {} seria de {:.2f}kg".format(pesoTerra,codPlaneta ,pesoPlaneta))

def nivel11():
    idade = int(input("Indique a sua idade: "))

    if idade >= 0 and idade <= 12:
        fase1 = "Infância"
        if idade >= 0 and idade <= 2:
            fase2 = "Primeira Infância"
        elif idade >= 3 and idade <= 6:
            fase2 = "Infância Intermediária"
        elif idade >= 7 and idade <= 12:
            fase2 = "Pré-adolescência"
    elif idade >= 13 and idade <= 19:
        fase1 = "Adolescência"
        if idade >= 13 and idade <= 14:
            fase2 = "Puberdade"
        elif idade >= 15 and idade <= 19:
            fase2 = "Adolescência Tardia"
    elif idade >= 20 and idade <= 59:
        fase1 = "Adultez"
        if idade >= 20 and idade <= 39:
            fase2 = "Jovem Adulto"
        elif idade >= 40 and idade <= 59:
            fase2 = "Meia-idade"
    else:
        fase1 = "Terceira Idade"
        if idade >= 60 and idade <= 74:
            fase2 = "Idosos Jovens"
        elif idade >= 75:
            fase2 = "Idosos Velhos"

    print("{} - {}".format(fase1, fase2))

opcao = int(input("Escolha um dos níveis: "))

match opcao:
    case 1:
        nivel1()
    case 2:
        nivel2()
    case 3:
        nivel3()
    case 4:
        nivel4()
    case 5:
        nivel5()
    case 6:
        nivel6()
    case 7:
        nivel7()
    case 8:
        nivel8()
    case 9:
        nivel9()
    case 10:
        nivel10()
    case 11:
        nivel11()
    case _:
        print("Tentar novamente")