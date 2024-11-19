def function(text):
    newword = ""
    for char in text:
        newword += char + "-"

    newword= newword.rstrip("-")
    return newword

print(function("UE"))