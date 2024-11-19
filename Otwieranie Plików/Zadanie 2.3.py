###
# Makes a copy of a text file
#

# file names
original_file = 'C:/Users/tomza/Desktop/Repository/prg-basics/08-FileHandling/healthy_lifestyle.txt'
target_file = 'C:/Users/tomza/Desktop/Programowanie/Python/Otwieranie Plików/copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file,'r') as ReadFile:
   content = ReadFile.read()
   array = content.split()


# write the content to the target file (copy)
with open(target_file,"w") as CopyFile:
   for item in array:
        CopyFile.write(item)
        CopyFile.write(" ")