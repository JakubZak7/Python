total_sum = 0
aritmetic = 0
number_count = 0
while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break
    total_sum += number
    aritmetic += number
    number_count += 1


aritmetic_value = aritmetic / number_count
print(f"The total sum of the numbers is: {total_sum}")
print(aritmetic_value)