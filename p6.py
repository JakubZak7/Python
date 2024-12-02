import json


def f(years, course, avarage_grade):
    count = 0

    with open("data.json", "r", encoding="UTF-8") as file:
        students = json.load(file)

        for student in students:
            if student["age"] >= years:
                for c in student["studies"]["courses"]:
                    if c["name"] == course:
                        avg = sum(c["grades"]) / len(c["grades"])
                        if avg >= avarage_grade:
                            count += 1
                        break
    return count


if __name__ == '__main__':
    print(f(21, "statistics", 4))
