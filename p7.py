#A valid username consists of 4 to 12 characters: lowercase letters,
# numbers and the underscore character. Define a function f(array) that,
# for a given array of usernames, returns the number of valid usernames in the array. Example:

# f(["uek","water_7_x","anna.may","a_b_c_d_e_f"])  2
import re


def f(array):
    counter = 0
    pattern = r"^[\d\w]{4,12}$"

    for username in array:
        if re.match(pattern,username):
            counter += 1

    return counter

if __name__ == "__main__":
    print(f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"]))