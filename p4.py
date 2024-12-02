# (p4.py) The dictionary contains the names of subjects and the grades obtained.
# Define a function f(subjects) that, for the given subjects and their grades,
# returns the name of the subject for which the average grade is the highest. Example:
# f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})  "comp"


def f(lista):
    best_subcject = None
    max = 0

    for key,values in lista.items():
        avg = sum(values) / len(values)

        if avg > max:
            max = avg
            best_subcject = key

    return best_subcject



if __name__ == '__main__':
    print(f({"math": [3, 4, 4], "geo": [5, 4, 4, 4], "comp": [5, 4]}))











