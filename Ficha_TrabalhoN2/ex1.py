#Fatorial de um número
num = int(input("Indique um número: "))

while num < 0:
    num = int(input("Indique um número superior a 0: "))

fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print("O fatorial de {} é {}".format(num, fatorial))