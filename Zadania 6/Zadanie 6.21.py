ammount = int(input("Type the ammount of money: "))
five_zloty = 0
two_zloty = 0
one_zloty = 0
word = ammount

if ammount // 5 > 0:
    five_zloty += ammount // 5
    ammount -= (ammount // 5 * 5)
if ammount // 2 > 0:
    two_zloty += ammount // 2
    ammount -= (ammount // 2 * 2)
one_zloty += ammount

print(f"The ammount of PLN {word} in coins")
print(f"5PLN coins: {five_zloty}")
print(f"2PLN coins: {two_zloty}")
print(f"1PLN coins: {one_zloty}")