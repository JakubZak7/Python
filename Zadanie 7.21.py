def function(text):
    skrot = ""
    skrot += text[0]

    for index in range(1,len(text)):
        if text[index] == " ":
            skrot += text[index+1]

    return skrot

print(function("Internet of Things"))
print(function("For Your Information"))