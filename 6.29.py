###
# 
# A natural number greater than 1 is called a prime 
# if it has exactly 2 natural factors with the values 1 and this number. 
# Write a program that finds N leading prime numbers. 
# Read the value of N from the keyboard. 
# Using loop statements check that the number N is divisible only by 1 and by N.

N = int(input('Enter N: '))

prime_count = 0    # to count how many primes we found
current_number = 2 # we're starting with first prime nuber 

print(f"The first {N} prime numbers are:")

while prime_count < N:
    is_prime = True
    for i in range(2, int(current_number ** 0.5) + 1):  # Check divisors up to the square root
        if current_number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(current_number)  # Print the prime number
        prime_count += 1  # Increment the count of primes found
    
    current_number += 1 