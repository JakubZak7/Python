x = int(input('Type x: '))
y = int(input('Type y: '))



if x > 0 and y > 0:
    print(f"P({x},{y}) are in first quadrant")
elif x > 0 and y < 0:
    print(f"P({x},{y}) are in fourth quadrant")
elif x < 0 and y > 0:
    print(f"P({x},{y}) are in second quadrant")
elif x < 0 and y < 0:
    print(f"P({x},{y}) are in third quadrant")
else:
    print(f"P({x},{y}) are on (0,0) point")



