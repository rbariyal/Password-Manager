
def encrypt(data, shift):
    encrypted = ""
    for i in range(len(data)):

        char = data[i]
        if(char.isupper()):
            encrypted += chr((ord(char)+shift - 65) % 26+65)
        elif(char.islower()):
            encrypted += chr((ord(char)+shift - 97) % 26+97)
        elif(char.isdigit()):
            number = (int(char)+shift) % 10
            encrypted += str(number)
        else:
            encrypted += char
    return encrypted


def decrypt(data, shift):
    decrypted = ""
    for i in range(len(data)):
        char = data[i]
        if(char.isupper()):
            decrypted += chr((ord(char)-shift - 65) % 26+65)
        elif(char.islower()):
            decrypted += chr((ord(char)-shift - 97) % 26+97)
        elif(char.isdigit()):
            number = (int(char)-shift) % 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted


menu = ""
while menu != 1 or menu != 2:
    menu = input("Would you like to save new password or view your old ones?"
                 "\n1.Input new password"
                 "\n2.View passwords\n")
    if menu == "1":
        softwarename = input("Enter the name of software:")
        username = input("Enter your username for this software:")
        password = input("Enter your password:")
        shift = 2
        file = open("securepassword.txt", "a")
        file.write(encrypt(softwarename, shift)+";|" +
                   encrypt(username, shift)+";|"+encrypt(password, shift)+"\n")
        file.close()
    if menu == "2":
        file = open("securepassword.txt", "r")
        print("Software\tUsername\tPassword")
        shift = 2
        for i in file:
            data = i.split(";|")
            print(decrypt(data[0], shift)+"\t", decrypt(data[1],
                  shift)+"\t", decrypt(data[2], shift))
    if menu == "3":
        exit()
