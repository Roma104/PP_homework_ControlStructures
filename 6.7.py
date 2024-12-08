#Write a program that asks the user for their age
#  then checks which age group they belong to:

#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

user_age = int(input('Enter your age: '))

if user_age < 13:
    print("User is a child.")
elif user_age >= 13 and user_age < 20:
    print("User is a teen.")
elif user_age >= 20 and user_age < 65:
    print("User is an adult.")
elif user_age >= 65:
    print("User is a senior.")
    