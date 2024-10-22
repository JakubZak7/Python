def sum_digits(number):
    sum = 0
    number = str(abs(number))
    for char in number:
        char = int(char)
        sum += char

    return sum

number = 123
print(sum_digits(number))

