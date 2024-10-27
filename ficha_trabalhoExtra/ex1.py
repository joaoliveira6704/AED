def romanNumeral(number):
    """
    Converts a number between 1-999 in roman
    """
    # Dicionário de correspondências para números romanos
    roman_dict = [
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    
    # Converte o número em um numeral romano
    for (value, symbol) in roman_dict:
        while number >= value:
            result += symbol
            number -= value
    
    return result

# Entrada do usuário
numero = int(input("Escreva um número (1-999): "))

while numero < 1 or numero > 999:
    numero = int(input("Escreva um número (1-999): "))

# Exibe o numeral romano
print(romanNumeral(numero))