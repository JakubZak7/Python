# C:\Users\tomza\Desktop\Repository\prg-basics\08-FileHandling
###
# Reads the entire contents of a file
#
def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

# reads the entire file
file_content = read_from_file('C:/Users/tomza/Desktop/Repository/prg-basics/08-FileHandling/countries.txt')

# splits the entire file contents into lines
# and stores them in an array
file_lines = file_content.splitlines()

file_lines.sort()

# prints the array
counter = 1
for line in file_lines:
   print(f"{counter}. {line}", end="")
   print("")
   counter += 1