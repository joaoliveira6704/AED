n = int(input("\t\tNº de termos a imprimir: "))
numA = 1
numB = 0
i = 0
numFibo = ''

while i < n-1:
    numFibo += str(numA) + " "
    num = numA + numB
    numB = numA
    numA = num
    i+=1

print("\n\t\tPrimeiro {} termos da sequência de Fibonacci: 0 {}".format(n, numFibo))
