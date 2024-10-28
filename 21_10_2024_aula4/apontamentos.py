#Funções

"""def function_name(parameters):
    "function docstring"
    statement1
    statement2
    ...
    ...
    return[expr]"""

def fatorial(num):
    """
    recebe um número como argumento, calculando o seu fatorial
    Args: num: -número inteiro
    """
    if num >= 0:
        fatorial=1
        for i in range(num,1,-1):
            fatorial *= i
            print("Fatorial de {:n} é {:n}".format(num, fatorial))
    else:
        print("Argumento não pode ser um inteiro negativo.")

def soma(num1, num2, num3):
    """
    recebe 3 numeros e soma-os.
    """
    somaNum = num1+num2+num3
    print("{:n} + {:n} + {:n} = {:n}".format(num1,num2,num3,somaNum))

numero = int(input("Indique um número: "))
fatorial(numero)
soma(10,20,30)

