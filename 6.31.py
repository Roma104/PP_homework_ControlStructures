###
#
#Write a program that prints 20 integer random numbers in the range of 5 to 10.
import random

for i in range (1,21):
    random_number = random.randint(5, 10)
    print(f'{random_number}')