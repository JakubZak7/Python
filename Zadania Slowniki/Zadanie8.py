price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
discount_percentage = 10 #10%
totalvalue = 0

for key,value in price_list.items():
    print(F"{key}: {value}")
    totalvalue += value
    
    price_list[key] = round(value - ((discount_percentage/100) * value),2)

print(f"Total value before discount: {round(totalvalue,2)}")

totalvalue = 0

for key,value in price_list.items():
    print(F"{key}: {value}")
    totalvalue += value

print(f"Total value after 10% discount: {round(totalvalue,2)}")