###
#A computer program analyses the price of a product in an online store. 
# If the product price decreases by at least 10%, 
# the program prints a purchase recommendation:
#
#Buy the product!!
#Product price reduced by 17%
#
#Create such program. The current and previous price of the product are included in variables. 
# 
# Sample result:
#

previous_price = 200.00
current_price = 140.00

difference = previous_price - current_price
procent = difference/previous_price * 100

if procent > 10:
    print("Buy the product!!")
    print(f'Product price reduced by {procent}%.')
else:
    print('Do not buy it, it is not worth it.')
#Buy the product!!
#Product price reduced by 30%
#

