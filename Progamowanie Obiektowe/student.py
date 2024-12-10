# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.passed = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.passed = "y"
    student2.name = "Olivia"
    student2.age = 21
    student2.passed = "n"
    student3 = Student()
    student3.name = "Jakub"
    student3.age = 19
    student3.passed = "y"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, Is he/she passed {student1.passed}')
    print(f'{student2.name}, {student2.age} years old, Is he/she passed {student2.passed}')
    print(f'{student3.name}, {student3.age} years old, Is he/she passed {student3.passed}')

if __name__ == "__main__":
    main()