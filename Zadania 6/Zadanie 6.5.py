###
# Program that simulates the operation of an electronic thermometer.
#
temperature = 0
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It is hot")
elif temperature >= 15:
    print("It is warm")
elif 15 > temperature >= 0:
    print("It is cold")
elif 0 > temperature:
    print("Warning it is cold")