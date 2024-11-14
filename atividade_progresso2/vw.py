cidades = ['Porto', 'Maia', 'Matosinhos', 'Vila do Conde', 'Póvoa de Varzim', 'Gondomar', 'Gaia']

temperaturas = []

def dadosEstatistica(temperaturas, cidades):
    media = sum(temperaturas) / len(temperaturas)
    maior_diferenca = 0  # Inicializa para armazenar a maior diferença
    tempLonge = temperaturas[0]  # Inicializa com o primeiro valor de temperatura

    for i in range(len(temperaturas)):
        diferenca = abs(temperaturas[i] - media)
        if diferenca > maior_diferenca:
            tempLonge = temperaturas[i]
            maior_diferenca = diferenca

    pos = temperaturas.index(tempLonge)
    cidade = cidades[pos]

    return f"\n\nTemperatura mais longe do valor médio: {cidade} - {tempLonge}ºC"


for i in range(len(cidades)):
    while True:
        try:
            temperaturaCidade = int(input(f"Insira a temperatura na cidade de {cidades[i]} (0-40)ºC: "))
            if 0 <= temperaturaCidade <= 40:
                temperaturas.append(temperaturaCidade)
                break
            else:
                print("Valor fora dos limites! Insira uma temperatura entre 0 e 40.")
        except ValueError:
            print("Valor inválido! Insira um número inteiro.")

print(dadosEstatistica(temperaturas, cidades))
