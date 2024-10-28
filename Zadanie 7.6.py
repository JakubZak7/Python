def checkisBinary(number):
    for char in number:
        if char != '0' and char != '1':
            return False

    return True

binary = input("Type binary number: ")
print(checkisBinary(binary))