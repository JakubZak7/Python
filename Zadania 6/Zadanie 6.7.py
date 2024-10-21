age = int(input("Type your age: "))

if age < 13:
    print("You are child")
elif 19 >= age >= 13:
    print("You are teen")
elif 64 >= age >= 20:
    print("You are adult")
elif age >= 65:
    print("You are senior")
else:
    print("You are dead")