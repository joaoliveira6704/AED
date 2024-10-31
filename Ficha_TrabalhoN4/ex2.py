import random

def generateNumbers(limInf, limSup, quantNum):
    """
    Generates Euromillions numbers and stars given a inferior and superior limit, aswell as a number quantity
    """
    chaveEuromilhoes = []
    estrelas = []

    if limSup == 50:
        for i in range(quantNum):
            number = random.randint(limInf,limSup)
            if number not in chaveEuromilhoes:
                chaveEuromilhoes.append(number)

        return chaveEuromilhoes
            
    if limSup == 12:
        for i in range(quantNum):
            number = random.randint(limInf,limSup)
            if number not in estrelas:
                estrelas.append(number)

        return estrelas


    
def gerarChave():
    print(f"Chave do Euromilhões = {generateNumbers(1,50,5)} Estrelas: {generateNumbers(1,12,2)}")

    jogar = input("Deseja gerar nova chave(S/N)?")

    if jogar.upper() == "S":
        gerarChave()
    else:
        exit()

gerarChave()