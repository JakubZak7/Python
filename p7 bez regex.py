#A valid username consists of 4 to 12 characters: lowercase letters,
# numbers and the underscore character. Define a function f(array) that,
# for a given array of usernames, returns the number of valid usernames in the array. Example:

# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2
import re


def f(array):
    counter = 0
    letter = 0
    specialword = 0

    for item in array:
        if 4 <= len(item) <= 12:
            for i in item:
                if i.islower():
                    letter += 1
                if i == "_":
                    specialword += 1
                    
        if letter != 0 and specialword != 0:
            counter += 1
            letter = 0
            specialword = 0

    return counter

if __name__ == "__main__":
    print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))