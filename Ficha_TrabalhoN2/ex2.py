limInf = int(input("Indique o limite inferior: "))
limSup = int(input("Indique o limite superior: "))
soma = 0

for i in range(limInf, limSup + 1):
    if i % 2 == 0:
        soma += i

print("A soma de todos os pares entre {} e {} é {}".format(limInf, limSup, soma))