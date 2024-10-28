fatorial = 1

number = int(input("Number: "))

for i in range(number, 0, -1):
    fatorial *= i

print(fatorial)