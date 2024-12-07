###
# Sums numbers entered by user
#
total_sum = 0
times = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    times += 1

aritmatic = total_sum/times
print(f"The total sum of the numbers is: {total_sum}")
print(f'The arithmatic sum of the numbers is:{aritmatic}')