num = int(input("Indique um número: "))

while num < 0:
    num = int(input("Indique um número positivo: "))
soma=0

for i in range(1, num):
    if (num % i == 0):
        soma += i
    
if soma == num:
    print("{} é número perfeito.".format(num))
else: 
    print("{} não é um número perfeito.".format(num))