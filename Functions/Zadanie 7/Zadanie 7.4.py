def checker(number,x,y):
    if x <= number <= y:
        return True
    else:
        return False

setNumber = int(input("Type number: "))
x = int(input("Type lower range cap:  "))
y = int(input("Type higer range cap: "))

print(f"Number {setNumber} in the range <{x},{y}>: {checker(setNumber,x,y)}")