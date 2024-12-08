###
#Most female names in Polish end with the letter "a". 
# Write a program that prints the name entered from the keyboard, provided it is a female name. 

# Sample result:
#Enter name: Anna
#Anna -- Polish female name

name = input('Enter name: ')
last_character = name[-1]

if last_character == 'a':
    print(f'{name} is a polish female name!')
else:
    print(f'{name} is not a polish female name.')
