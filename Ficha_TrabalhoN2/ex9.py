n = int(input("Quantos números deseja ler? "))

numMaior = None
segMaior = None

for i in range(n):
    num = int(input("Número: "))

    if numMaior is None:  
        numMaior = num
    elif num > numMaior:  
        segMaior = numMaior  
        numMaior = num  
    elif segMaior is None or num > segMaior: 
        segMaior = num  

print("\n\n\t\tSegundo maior número da lista de número lidos é:", segMaior)
