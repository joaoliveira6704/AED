def pluviosidade(pluvMeses):
    pluvSorted = sorted(pluvMeses, reverse=True)
    
    resultado = ""
    print("\n\nMês:           Chuva:")
    for chuva, mes in pluvSorted:
        resultado += f"{mes} ->   {chuva}\n"
    
    return resultado

meses = ['Janeiro   ', 'Fevereiro ', 'Março     ', 'Abril     ', 'Maio      ', 'Junho     ', 'Julho     ', 'Agosto    ', 'Setembro  ', 'Outubro   ', 'Novembro  ', 'Dezembro  ']

mesesPluv = []

for i in range(len(meses)):
    valorPluv = int(input(f"Pluviosidade no mês de {meses[i]}: "))
    mesesPluv.append((valorPluv, meses[i]))

print(pluviosidade(mesesPluv))