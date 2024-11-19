###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'
counter = 1
with open('C:/Users/tomza/Desktop/Repository/prg-basics/08-FileHandling/it_company.csv','r') as ReadFile:
   for line in ReadFile:
      if job_title in line:
         print(f"{counter}. {line}",end=" ")
         counter += 1