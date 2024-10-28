def sumNumbers(number,value):
    sum = 0
    number = str(number)
    if value == True:
        for i in number:
            if int(i) % 2 == 0:
                sum += int(i)
    elif value == False:
        for i in number:
            if int(i) % 2 != 0:
                sum += int(i)
    else:
        return "Type correctly value, and try again"

    return sum


print(sumNumbers(20576,False))


