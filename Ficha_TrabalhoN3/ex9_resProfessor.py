def printCharLine(texto, numCar):
	while(len(texto)>numCar):
		print(texto[:numCar])
		texto=texto[numCar:]
	print(texto)

texto=input("Texto a imprimir: ")
numChar=int(input("Número de caracteres a imprimir por linha: "))
printCharLine(texto,numChar)