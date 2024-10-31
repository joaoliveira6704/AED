def pluviosidade(pluv, meses):
    pluv.sort(reverse=True)

    return pluv

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

listPluv = []

for mes in meses:
    valorPluv = int(input(f"Pluviosidade no mês de {mes}: "))
    listPluv.append(valorPluv)

print(pluviosidade(listPluv, meses))