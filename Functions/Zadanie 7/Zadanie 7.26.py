def funkcja(text):
    suma = 0
    dlugosctext= len(text)

    for i in range(0,len(text)-1):
        suma += int(text[i])

    warunek = int(text[dlugosctext-1])

    if suma % 7 == warunek:
        return True
    else:
        return False

print(funkcja("1114"))
