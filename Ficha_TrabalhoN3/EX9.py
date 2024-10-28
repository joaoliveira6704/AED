def printChartLine(texto,numeroCar:int):
    textoList = []

    texto = []
    texto.append(texto)

    while len(texto) > numeroCar:
        textoList.append(texto[:numeroCar])
        texto = texto[numeroCar:]
    
    for i in textoList:
        return i


texto = input("Texto: ")
numeroCar = int(input("Número de caracteres a imprimir por linha: "))
print(printChartLine(texto,numeroCar))