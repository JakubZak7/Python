def return_month(number):
    month = ""
    if number == 1:
        month = "January"
    elif number == 2:
        month = "February"
    elif number == 3:
        month = "March"
    elif number == 4:
        month = "April"
    elif number == 5:
        month = "May"
    elif number == 6:
        month = "June"
    elif number == 7:
        month = "July"
    elif number == 8:
        month = "August"
    elif number == 9:
        month = "September"
    elif number == 10:
        month = "October"
    elif number == 11:
        month = "November"
    elif number == 12:
        month = "December"

    return month

number = int(input("Select number of month: "))

print(f"The nae of month {number} is {return_month(number)}")
