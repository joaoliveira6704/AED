def maior(nums):
    """
    Returns the biggest in a list
    """
    maiorN = nums[0]
    for i in range(len(nums)):
        if nums[i] > maiorN:
            maiorN = nums[i]
    return maiorN

soma = []

quantNum = int(input("Insira a quantidade de números a introduzir"))

for i in range (quantNum):
    num = int(input("Número:"))
    soma.append(num)

print(maior(soma))