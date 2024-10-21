###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0
n = N
# Calculate the sum of even numbers
while N > 0:
    if N % 2 == 0:
        sum_even += N
    N -= 1

print(f"The sum of even numbers from 1 to {n} is: {sum_even}")