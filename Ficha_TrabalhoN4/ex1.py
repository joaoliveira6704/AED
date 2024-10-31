def aboveAverage(numbers):
    """
    Returns average and numbers above average in a list with 10 numbers
    """
    average = sum(numbers) / 10

    numberStr = ''

    for number in numbers:
        if number > average:
            numberStr += str(number) + ' '

    return f'Média = {average}\nNúmeros acima da média: {numberStr}'

numberList = []
for i in range(0, 10):
    number = int(input(f"Número {i+1}:"))
    numberList.append(number)

print(aboveAverage(numberList))