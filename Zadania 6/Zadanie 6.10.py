dogY = int(input("Type dog years in human years: "))
sum = 0
for i in range(1,dogY+1):
    if i == 1 or i == 2:
        sum += 10.5
    else:
        sum += 4

    i += 1
print(f"The dog age in dog years are {int(sum)} years")