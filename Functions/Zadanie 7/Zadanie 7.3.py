def check_letter_e(text):
    counter = 0
    text = text.lower()
    for char in text:
        if char == "e":
            counter += 1

    return counter

text = input("Type text: ")
print(f"The nuber of letter 'e': {check_letter_e(text)}")