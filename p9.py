# The file data.csv contains a list of employees of the company ABC-Data.
# Define a function f(value) that returns the number of employees whose salary is greater than or equal to the given value. Example:
# f(9200)  compare your result with other students
# f(11640)  compare your result with other students

import csv

def f(value):
    count = 0

    with open("data.csv","r",newline='',encoding="utf-8") as file:
        csv_reader = csv.reader(file)

        next(csv_reader)

        for row in csv_reader:
            salary = float(row[9])

            if salary >= value:
                count += 1

    return count

if __name__ == "__main__":
    print(f(9200))
    print(f(11640))