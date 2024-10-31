def positiveList(pontuacao):
    """
    Returns the positive grades (>=10) in a list of 10 numbers 
    """
    pontPositiva = []
    for number in pontuacao:
        if number >= 10:
            pontPositiva.append(number)
    
    return f"Pontuações positivas: {pontPositiva}"

pontuacao = []

for i in range(0,10):
    try:
        addPontuacao = int(input("Pontuação: "))
    except:
        addPontuacao = int(input("Pontuação (inteiro!): "))
    
    pontuacao.append(addPontuacao)

print(positiveList(pontuacao))