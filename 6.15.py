###
#
#EAN-13 (European Article Number) is a barcode for marking goods. 
# The first 3 digits (590) usually indicate goods manufactured in Poland. 
# Write a program that checks whether the EAN-13 number 
# entered from the keyboard consists of exactly 13 characters (digits). 
# Print a message if the number is correct. 
# Additionally, only when the article number is correct, 
# print a message when the product was manufactured in Poland. 
# 
# Sample result:
#
#Enter EAN-13 article number: 5901230094938
#Article manufactured in Poland
#

EAN = input('Enter EAN-13 article number: ')

if len(EAN) == 13:
    print('Correct lenght of number.')
    if EAN[0] == '5' and EAN[1] == '9' and EAN[2] == '0':
        print('This article was manufactured in Poland.')
    else:
        print("This article was NOT manufactured in Poland.")

else:
    print("Wrong lenght of number.")