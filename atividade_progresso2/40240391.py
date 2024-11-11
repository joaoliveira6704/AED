cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

temperaturas = []

def dadosEstatistica(temperaturas, cidades):
    media = sum(temperaturas) / len(temperaturas)
    menor_diferenca = abs(temperaturas[0] - media)

    for i in range(1, len(temperaturas)):
        diferenca = abs(temperaturas[i] - media)
        if diferenca > menor_diferenca:
            tempLonge = temperaturas[i]
            menor_diferenca = diferenca

    pos = temperaturas.index(tempLonge)

    cidade = cidades[pos]

    return f"\n\nTemperatura mais longe do valor médio: {cidade} - {tempLonge}ºC"


for i in range(len(cidades)):
    try:
        temperaturaCidade = int(input(f"Insira a temperatura na cidade de {cidades[i]} (0-40)ºC: "))
    except ValueError:
        temperaturaCidade = int(input(f"Insira a temperatura na cidade de {cidades[i]} (0-40)ºC: "))
    else:
        while temperaturaCidade < 0 or temperaturaCidade > 40:
            temperaturaCidade = int(input(f"Valor fora dos limites! Insira a temperatura na cidade de {cidades[i]} (0-40)ºC: "))
    
    temperaturas.append(temperaturaCidade)

print(dadosEstatistica(temperaturas, cidades))