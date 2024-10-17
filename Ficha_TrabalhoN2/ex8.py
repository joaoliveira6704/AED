num = int(input("Indique um número entre 1 e 99: "))

numBin = ""
i=1

while num < 1 | num > 99:
    num = int(input("Indique um número entre 1 e 99"))

while i>0:
    i = num/2
    print(i)
    if ((i) - int(i) == 0.5):
        numBin += "1 "
        num = int(i)
    else:
        numBin += "0 "
        num = int(i)

num_Real = numBin[::-1]
char = num_Real[3:]

print(char)