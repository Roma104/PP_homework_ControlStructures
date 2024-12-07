###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
M = N
sum_even = 0


while True:
# Calculate the sum of even numbers
    if N == 0:
        break        
    if N % 2 == 0:
            sum_even += N
    N -= 1

print(f"The sum of even numbers from 1 to {M} is: {sum_even}")