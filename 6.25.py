###
#
#Write a program that creates the following pattern. Sample result:

#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999

rows = int(input("Enter number of rows: "))
row = 1
for i in range(1, rows + 1):
    print(f"{row} " * i)
    row += 1