###
#
#Write a program that converts a decimal number into a binary number. 
# To convert a decimal number to binary, follow these steps:
#
#Read a decimal number from the keyboard.
#Divide the number by 2 and note the remainder.
#Divide the quotient obtained by 2 and note the remainder.
#Repeat the same process till we get 0 as the quotient.
#Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
#Sample result:
#
#Enter decimal number: 12
#12(10) = 1100(2)

decimal_number = int(input("Enter decimal number: "))

binary_number = ""

original_number = decimal_number

# Convert decimal to binary by repeatedly dividing by 2
while decimal_number > 0:
    remainder = decimal_number % 2  
    binary_number = str(remainder) + binary_number  # Append the remainder at the start
    decimal_number = decimal_number // 2  # Update the number by integer division

print(f"{original_number}(10) = {binary_number}(2)")
