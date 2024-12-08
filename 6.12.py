###
# In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price from the keyboard. 
# 
# Sample result:
#
#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00
#

number_of_purchases = 5
price = 40

if number_of_purchases > 2:
    new_price = price * 0.75
    full_price = new_price * (number_of_purchases - 2) + 2 * price
else:
    full_price = price * number_of_purchases

print(f'Your total is {full_price} pln.')
