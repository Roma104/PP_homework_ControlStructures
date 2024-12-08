###
#Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. 
# 
# Sample result:
#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

time_in_24 = input('Enter time (24-hour format): ')

first_index = int(time_in_24[0])  
second_index = int(time_in_24[1]) 

hour = first_index*10 + second_index

if hour <= 12:
    print(f'It is {time_in_24} am.')
else:
    new_hour = hour - 12
    rest = time_in_24[2] + time_in_24[3] + time_in_24[4]
    print(f'It is {new_hour}{rest} pm.')