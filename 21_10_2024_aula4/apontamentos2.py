def primo(numero):
    """
    Recebe um número, verifica se é primo e devolve um boolean.
    Args: numero inteiros
    Returns: boolean (True, False)
    """
    primo=True
    for i in range(2, numero):
        if numero%i==0:
            primo=False
            break
    return primo

numero = int(input("Número para teste: "))
estado = primo(numero)
if estado == "True":
    print("Primo")
else:
    print("Não primo")