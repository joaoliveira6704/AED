#TRY AND EXCEPT STATEMENTS

try:
    int(input("Número: "))
    print(True)
except ValueError:
    print("Deve ser um número!")
    print(False)

###############------##################

numero = 10
try:
    divisor = int(input("Número: "))
    divisao = numero/divisor
except ZeroDivisionError:
    print("Divisão por zero não é possível!")
except:
    print("Não é possivel efetuar a divisão!")
else:
    print("Não ouve erros!")
finally:
    print("Executado sempre no fim!")