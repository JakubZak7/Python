def decimal_to_binary(n):
    binary = ""
    while n >0:
        binary = str(n%2) + binary
        n //= 2
    return binary

decimal_number = int(input("Type decimal number: "))

print(decimal_to_binary(decimal_number))