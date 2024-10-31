def positiveList(nome, pontuacao):
    """
    Returns the positive grades (>=10) in a list of 10 numbers 
    """
    nomePositiva = []
    pontPositiva = []
    for number in pontuacao:
        if number >= 10:
            numberIndex = pontuacao.index(number)
            pontPositiva.append(number)
            nomePositiva.append(nome[numberIndex])
    
    return f"Nomes: {nomePositiva}\nPontuações positivas: {pontPositiva}"

pontuacao = []
nomes = []

for i in range(0,10):
    nome = input("Nome: ")
    try:
        addPontuacao = int(input("Pontuação: "))
    except ValueError:
            addPontuacao = int(input("Pontuação (inteiro!): "))
    finally:
        nomes.append(nome)
        pontuacao.append(addPontuacao)

print(positiveList(nomes, pontuacao))