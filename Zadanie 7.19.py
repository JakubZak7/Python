def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if is_prime(num):
            count += 1

    return num

n = 5
result = f(n)
print(result)