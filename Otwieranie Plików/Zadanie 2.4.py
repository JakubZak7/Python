###
# Saves to a file a list of employees working at a specified position.
#

# file names
employees_file = 'C:/Users/tomza/Desktop/Repository/prg-basics/08-FileHandling/it_company.csv'
position_file = 'C:/Users/tomza/Desktop/Programowanie/Python/Otwieranie Plików/software_engineer.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file,'r') as ReadFile:
   with open(position_file,'w') as WriteFile:
      for line in ReadFile:
        if job_title in line:
            WriteFile.write(line)
            WriteFile.write(" ")