def checker(value):
    counter = 0
    for char in range(0,len(value)):
        if value[char] == "+":
            counter += 1
            if counter >= 3:
                return True
        elif value[char] == "-":
            counter -= 1

    return False


print(checker("+-++-++-+---"))
