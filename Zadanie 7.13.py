def operatorQuest(number1,number2,operator):
    if operator == "+":
        return number1 + number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    elif operator == "*":
        return number1 * number2
    elif operator == "-":
        return number1 - number2
    else:
        print("Type correct operator")


print(operatorQuest(2,3,"-"))