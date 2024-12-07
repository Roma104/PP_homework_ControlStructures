###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#

value_input = int(input('Enter falue 1/ : '))
value = value_input

for i in range(value % 2 == 0):
    value = 1/value
    
print(f'1/{value_input} = {value}')