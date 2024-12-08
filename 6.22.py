###
#
#Write a program that prints numbers from 1 to 30. 
# If the number is divisible by 3 then the program prints the word 'THREE'. 
# Next, if the number is divisible by 5 then the program prints the word 'FIVE'. 
# Finally, if the number is divisible by both 3 and 5 then the program prints the word 'BINGO'. 
# Sample result:

#1 2 THREE 4 FIVE THREE 7 ...

import time

countdown = int(input("Enter the number of seconds to count down: "))
start = 1

while countdown > 0 :
    if start % 5 != 0 and start % 3 != 0:
        print(start)
        countdown -= 1
        start += 1
        time.sleep(1)  # Wait for 1 second
    elif start % 5 == 0 and start % 3 != 0:
        print("FIVE!")
        countdown -= 1
        start += 1
        time.sleep(1)
    elif start % 5 != 0 and start % 3 == 0:
        print("THREE!")
        countdown -= 1
        start += 1
        time.sleep(1)
    elif start % 5 == 0 and start % 3 == 0:
        print("BINGO!")
        countdown -= 1
        start += 1
        time.sleep(1)

#print("Time's up!")