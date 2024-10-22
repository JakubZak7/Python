import math

def heron_triangle(a,b,c):
    s = (a+b+c) / 2
    area = int(math.sqrt(s*(s-a)*(s-b)*(s-c)))

    return area

print(f"3,4,5 result is {heron_triangle(3,4,5)}")
print(f"5,12,13 result is {heron_triangle(5,12,13)}")
print(f"7,24,25 result is {heron_triangle(7,24,25)}")
