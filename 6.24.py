###
#
#Write a program that creates the following pattern. Sample result:

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*

#Defining max point of stars
max_amount = 5

#first half of the pattern
for i in range(1, max_amount + 1):
    print("* " * i)

#second half of the pattern

for i in range(max_amount - 1, 0, -1):
    print("* " * i)