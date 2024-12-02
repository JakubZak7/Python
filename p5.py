# (p5.py) Define a function f(first_letter,last_letter) that, for the data.txt file,
# returns
# the number of words that start with the first_letter and end with the last_letter. Example:
import re


def f(first_letter, last_letter):
    # Initialize counter for matches
    counter = 0

    # Open and read the file
    with open("data.txt", "r", encoding="UTF-8") as readFile:
        # Iterate through each line in the file
        for line in readFile:
            # Extract words using regex (words are sequences of alphanumeric characters)
            words = re.findall(r'\b\w+\b', line)
            # Check each word
            for word in words:
                if word.startswith(first_letter) and word.endswith(last_letter):
                    counter += 1

    return counter


if __name__ == '__main__':
    print(f("w", "d"))
    print(f("a","d"))
