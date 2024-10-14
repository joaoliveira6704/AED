soma=0
numeroLista = []
for i in range(10):
    numeroPedido = int(input("Indique o {}º número (<20): ".format(i+1)))
    while numeroPedido > 20:
        numeroPedido = int(input("Indicou um número >20! Indique o {} número (<20): ".format(i+1)))
    soma+=numeroPedido
    numeroLista.insert(i, numeroPedido)

numMaior = numeroLista[0]

for r in numeroLista:
    if r > numMaior:
        numMaior = r

print("Média = {:n}\nMaior = {}".format(soma/10, numMaior))