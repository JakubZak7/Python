ean13_code = input("Type ean code: ")

if int(len(ean13_code)) == 13 and ean13_code.isdigit():
    print("Aritcle number is corret")

if ean13_code[:3] == '590':
    print("Article manufactured in Poland")