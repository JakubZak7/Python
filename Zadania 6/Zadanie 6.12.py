numberOfProducts = int(input("Amount: "))
productPrice = int(input("Price: "))


if numberOfProducts > 2:
    discounted_products = numberOfProducts - 2
    discount = 0.25 * productPrice
    sum = (2* productPrice) + (discounted_products * (productPrice - discount))
else:
    sum = numberOfProducts * productPrice

print(sum)