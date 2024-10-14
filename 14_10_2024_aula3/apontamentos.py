#####Ciclo FOR

#IMPRIMIR LISTA COM 1º - POSICAO1, ETC...
lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(10):
    print("{} - {}".format(i+1, lista[i]))

print("\n")

#i vai de 1 a 20, de 2 em 2 crescente
for i in range(1, 20, 2):
    print(i)

print("\n")

#i vai de 20 a 0, de 2 em 2 decrescente
for i in range(20, 0, -2):
    print(i)

print("\n")

#Imprimir caracteres numa string
nome = "Carla Caldeira"

for caracter in nome:
    print(caracter)

print("\n")

#Imprimir caracteres numa string na mesma linha

nome = "Carla Caldeira"

for caracter in nome:
    print(caracter, end="")

print("\n")



######Ciclo WHILE
numero = 1

while numero <= 10:
    print(numero)
    numero+=1

print("\n")

#Exemplo de estruturas repetitivas/ iterativas 

numero = int(input("Indique um número entre [0-20]: "))

while numero <= 0 or numero > 20:
    print("Número Inválido! Tente novamente")
    numero = int(input("Indique um número entre [0-20]: "))

print("\n")

#Tabuada

tabuada = int(input("Indique um número: "))
numero=1

while numero<11:
    print("{:n} x {:n} = {:n}".format(tabuada, numero, tabuada*numero))
    numero += 1

print("\n")

#Exemplos de estruturas repteitivas
import random

numGerado = random.randint(0,20)

numPalpite = int(input("Insira um número entre 0 e 20: "))

tentativas = 1

while numGerado != numPalpite:
    print("Não Acertou, o número era {} Tente novamente!".format(numGerado))
    numGerado = random.randint(0,20)
    numPalpite = int(input("Insira um número entre 0 e 20: "))
    tentativas+=1

print("Acertou o número {} em {} tentativas".format(numPalpite, tentativas))

print("\n")

###Quebra de ciclo

#break

tabuada = int(input("Indique um número: "))
numero=0

while numero<10:
    numero+=1
    if numero == 6:
        break
    print("{:n} x {:n} = {:n}".format(tabuada, numero, tabuada*numero))

print("\n")

#continue

tabuada = int(input("Indique um número: "))
numero=1

while numero<11:
    numero+=1
    if numero == 6:
        continue
    print("{:n} x {:n} = {:n}".format(tabuada, numero, tabuada*numero))

print("\n")