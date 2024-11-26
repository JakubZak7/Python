items = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

totalnumberofproducts = 0

newlist = {
    
}

for key, value in items.items():
    newlist[key] = value
    totalnumberofproducts += value
    
    
print(f"Total number of products: {totalnumberofproducts}")


for key,value in newlist.items():
    print(f"Item: {key}, Quantity: {value}")