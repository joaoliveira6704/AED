import random

def generatePassword(userName):

    for i in range(len(userName)):
        if i % 2 != 0:
            while i >= 0:
                password = userName[i] + str(random.randint(1,9))
                i-=1
        
    for i in range(len(password)):
        while len(password) < len(userName):
            password += str(random.randint(1,9))
            break

    return password

userNameInput = input("Username: ")

spaces = userNameInput.count(" ")

while spaces >= 1:
    print("User name não pode ter espaços!! Tente novamente.")
    userNameInput = input("Username: ")
    spaces = userNameInput.count(" ")

print(generatePassword(userNameInput))