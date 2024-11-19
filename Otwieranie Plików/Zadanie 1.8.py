def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content


file_content = read_from_file("C:/Users/tomza/Desktop/Repository/prg-basics/08-FileHandling/pets.txt")
file_lines = file_content.split()

text = ""
TextWordsLen = len(file_lines)

for line in file_lines:
    text += line
    text += " "
    
print(f"{text} and the text has {TextWordsLen} words.")