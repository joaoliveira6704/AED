import random

numRand = random.randint(0, 50)
numIns = int(input("Insira um número entre 0 e 50: "))

tentativas = 0

while (numIns > 50) | (numIns < 0):
    numIns = int(input("Insira um número entre 0 e 50: "))

while numRand != numIns:
    if tentativas <= 10:
        if numIns < numRand:
            print("Número é maior")
            numIns = int(input("Insira um número entre 0 e 50: "))
            tentativas += 1
        else:
            print("Número é menor")
            numIns = int(input("Insira um número entre 0 e 50: "))
            tentativas += 1
    else:
        print("Esgotou as 10 tentativas :(")
        exit()


if numIns == numRand:
    print("Parabéns! Acertou!")


