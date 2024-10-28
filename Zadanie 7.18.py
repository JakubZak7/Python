def sumNumbers(number):
    number = str(number)
    sum = 0

    for char in number:
        sum += int(char)

    return sum


print(sumNumbers(2137))