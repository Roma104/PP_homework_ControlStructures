###
#
#There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

#Enter the amount in PLN: 18
#The amount of PLN 18 in coins:
#5 PLN coins: 3
#2 PLN coins: 1
#1 PLN coins: 1

amount = int(input('Enter the amount in PLN: '))

coin_5 = amount // 5
rest_5 = amount % 5

coin_2 = rest_5 // 2
coin_1 = rest_5 % 2

print("The amount of PLN 18 in coins:")
print(f'5 PLN coins: {coin_5}')
print(f'2 PLN coins: {coin_2}')
print(f'1 PLN coins: {coin_1}')
