import keyboard_input

# Reads employee's data from keyboard
first_name = keyboard_input.input_string('Enter name: ')
last_name = keyboard_input.input_string('Enter lastname: ')
age = keyboard_input.input_integer('Enter age: ')
salary = keyboard_input.input_real('Enter salary: ')
is_salary_hidden = keyboard_input.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Lastname: ', last_name)
print('Age: ', age)
if not is_salary_hidden:
    print('Salary', salary)
else:
    print("Hidden")
