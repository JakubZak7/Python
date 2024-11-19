###
# Reads from file, line by line
#
with open('C:/Users/tomza/Desktop/Repository/prg-basics/08-FileHandling/countries.txt', 'r') as file:
    counter = 1
    for line in file:
        print(f"{counter}. {line}",end="")
        counter += 1