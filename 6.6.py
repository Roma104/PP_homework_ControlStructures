###
#The parking meter calculates the parking fee based on the number of hours the car 
# was parked according to the following rules:

#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN
#Write a program that asks for the number of hours of parking, 
# then calculates and prints the correct fee.
###

car_on_parking = int(input('Enter how long you are staying on the parking lot: '))

if car_on_parking <= 2:
    fee = 5
elif car_on_parking > 2 and car_on_parking <= 6:
    fee = 15
else:
    fee = 20

print(f'Your fee for parking is {fee} pln.')

