def somatorio(numInf:int,numSup:int):
    """
    Returns the sum of a list of numbers
    Args: int number, int number
    """
    soma = 0
    for i in range(numInf,numSup+1):
        soma += i
    
    print("Somatório de {:n} a {:n} = {:n}".format(numInf, numSup, soma))

numInf = int(input("Limite Inferior: "))
numSup = int(input("Limite Superior: "))
somatorio(numInf, numSup)

