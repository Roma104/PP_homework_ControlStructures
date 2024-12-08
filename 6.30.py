###
#
#Write a program that prints a lottery coupon (numbers from 1 to 49) in the format as below.

#1 8 15 22 29 36 43
#2 9 16 23 30 37 44
#3 10 17 24 31 38 45
#4 11 18 25 32 39 46
#5 12 19 26 33 40 47
#6 13 20 27 34 41 48
#7 14 21 28 35 42 49


for row in range(1, 9):  # Rows from 1 to 7
    for column in range(row, 50, 7):  # Step of 7 to print numbers in the column
        print(f"{column:2}", end=" ")  # Print numbers with proper spacing
    print()  # Move to the next line after each row