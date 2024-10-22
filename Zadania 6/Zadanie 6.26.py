PIN = "0805"

TryPIN = input("Type pin: ")

if TryPIN == PIN:
    print("Logged in")
else:
    print("Try again")
    TryPIN = input("Type pin: ")
    if TryPIN == PIN:
        print("Logged in")
    else:
        print("Try again")
        TryPIN = input("Type pin: ")
        if TryPIN == PIN:
            print("Logged in")
        else:
            print("Incorrect")
            print("Your payment is blocked")

