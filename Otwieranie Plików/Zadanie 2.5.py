# Creates a shopping list based on product names
# entered from the keyboard.
#

# shopping list file name
shopping_list = 'C:/Users/tomza/Desktop/Programowanie/Python/Otwieranie Plików/shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
   with open(file_name,'a') as WriteFile:
      WriteFile.write(product_name)
      WriteFile.write("\n")

# Takes next product name from the keyboard
product = ""
while product != "0":
   product = input('Enter product name (0 stops): ')
   if product == '0':
      break
   else:
      add_product(shopping_list,product)
