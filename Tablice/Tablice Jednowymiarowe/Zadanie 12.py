categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max = 0

for item in expenses:
    if item > max:
        max = item
        

for index in range(0,len(expenses)-1):
    if expenses[index] == max:
        print(categories[index])