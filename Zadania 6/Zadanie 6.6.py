hours = int(input("Type how many hours you stayed: "))
money = 0
if 2 >= hours >= 1:
    money = 5
elif 6 >= hours >= 3:
    money = 15
elif hours > 6:
    money = 20

print(f"You need to pay {money} PLN")