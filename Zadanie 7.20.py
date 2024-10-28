def checkGap(n1, n2, n3):
    max = 0
    min = 0

    if n1 > n2 and n1 > n3:
        max = n1
    elif n2 > n1 and n2 > n3:
        max = n2
    elif n3 > n1 and n3 > n2:
        max = n3

    if n1 < n2 and n1 < n3:
        min = n1
    elif n2 < n1 and n2 < n3:
        min = n2
    elif n3 < n1 and n3 < n2:
        min = n3

    return max - min

print(checkGap(1,2,10))
