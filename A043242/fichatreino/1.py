import os
os.chdir("fichatreino")
cwd = os.getcwd()

continentes = ['África', 'Europa', 'América', 'Oceania', 'Ásia', 'Antártica']

if not os.path.exists("ficheiros"):
    os.mkdir("ficheiros")

f = open(cwd+"\\ficheiros\\texto.txt", "a")

pais = input("Escreva o pais: ")
continente= input("Escreva o continente: ")
while continente not in continentes:
    continente= input("Escreva o continente: ")

texto = pais + ";" + continente + "\n"

f.write(texto)
f.close()

f = open(cwd+"\\ficheiros\\texto.txt", "r")

t = f.readlines()
for line in t:
    campos = line.split(";")
    print(f"{campos[1].strip("\n")}: {campos[0]}")
f.close()