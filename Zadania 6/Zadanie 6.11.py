currentPrice = int(input("Type current price: "))
previousPrice = int(input("Type previous price: "))

discount = int((previousPrice-currentPrice)/previousPrice * 100)

print("BUY THE PRODUCT!!!")
print(f"Product is reduced by {discount} %")