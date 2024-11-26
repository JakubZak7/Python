translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}


word = input("Type the word in english: ")

for key, value in translations.items():
    if key == word:
        print(value)