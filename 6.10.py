###
#Write a program that calculates a dog's age in dog's years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years. 
# 
# Sample result:
#Enter the dog's age in human years: 15
#The dog's age in dog's years is 73 years.

human_years = int(input('Enter the dogs age in human years: '))
dog_years = 0

if human_years <= 2:
    dog_years = 10.5 * human_years
else:
    dog_years = (human_years-2) * 4 + 21

print(f'The dogs age in dogs years is {dog_years} years.')