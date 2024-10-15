plain_text = "The early bird catches the worm"
encrypted_text = ''

for char in plain_text:
    newLetter = chr(ord(char)+1)
    encrypted_text += newLetter

print(encrypted_text)



# Real Ceasar Code
def CeasarEncrypted(plain_text,encrypted_text,shift):
    encrypted_text = ""
    for char in plain_text:
        if (char.isupper()):
            encrypted_text += chr((ord(char)+shift-65) % 26 + 65)

        else:
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)

    return encrypted_text


plain_text = "ATTACKATONCE"
shift = 4
encrypted_text = ""

print(CeasarEncrypted(plain_text,encrypted_text, shift))
