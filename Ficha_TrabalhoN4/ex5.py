def mesMax(meses, faturacao):
    maiorFat = max(faturacao)

    for number in faturacao:
        if number == maiorFat:
          pos = faturacao.index(number)
          mesMax = meses[pos]

    return mesMax

def mesMin(meses, faturacao):
    menorFat = min(faturacao)

    for number in faturacao:
        if number == menorFat:
          pos = faturacao.index(number)
          mesMin = meses[pos]

    return mesMin

def fatMed(faturacao):
    faturacaoMedia = sum(faturacao) / len(faturacao)

    return round(faturacaoMedia, 2)

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

faturacao = []

for mes in meses:
    faturacaoInput = int(input(f"Faturação de {mes}: "))
    faturacao.append(faturacaoInput)

print(f"Mês de maior faturação: {mesMax(meses, faturacao)}\n")
print(f"Mês de menor faturação: {mesMin(meses, faturacao)}\n")
print(f"Valor médio faturação: {fatMed(faturacao)}\n")