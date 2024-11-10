def ordenarVisitas(valor, dias):
    visitasOrdenadas = []

    for i in range(len(dias)):
        visitasOrdenadas.append((valor[i], dias[i]))
    
    visitasOrdenadas = sorted(visitasOrdenadas, reverse=True)
    
    resultado = ""
    for valor, dias in visitasOrdenadas:
        resultado += f"{dias}: {valor}\n"
    
    return f"\n\nValores Ordenados: \n\n{resultado}"

def mediaVisitas(valor):
    return f"Média de visitas diárias: {sum(valor)/len(valor):.2f}"

def encontrarMaisProximoDaMedia(valor, dias):
    media = sum(valor) / len(valor)
    dia_mais_proximo = dias[0]
    menor_diferenca = abs(valor[0] - media)

    for i in range(1, len(valor)):
        diferenca = abs(valor[i] - media)
        if diferenca < menor_diferenca:
            dia_mais_proximo = dias[i]
            menor_diferenca = diferenca

    return f"Dia mais próximo do valor médio: {dia_mais_proximo}"

dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

valor = []

for i in range(len(dias)):
    valorVisita = int(input(f"{dias[i]}: "))
    valor.append(valorVisita)

print(ordenarVisitas(valor, dias))
print(mediaVisitas(valor))
print(encontrarMaisProximoDaMedia(valor, dias))