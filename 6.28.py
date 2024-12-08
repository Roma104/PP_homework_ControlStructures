###
#
#Write a program that prints the first twenty words of the Fibonacci sequence. 
# The sequence is defined as follows: the first term is equal to 0, 
# the second is equal to 1, each subsequent term is the sum of the previous two. 
# Sample result:

first_number = 0
second_number = 1
amount = int(input("Enter for how long you want this to go: "))

for i in range(1,amount+1):
    print(first_number)  # Print the current Fibonacci number
    # Update the numbers for the next iteration
    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number
