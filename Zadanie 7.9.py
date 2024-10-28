def function(x,y):
    counter = 0
    for i in range(x,y):
        if i % 2 == 0 and i < 0:
            counter += 1

    return counter

print(function(-1,11))
