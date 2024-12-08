###
#
#Yes-no question are often used in surveys to gauge people's attitudes 
# with regard to specific ideas or beliefs. 
# Write a program that prints a survey consisting of three questions. 
# Save the answers to logical type variables. Then view the survey result. 
# 
# Sample result:
#
#SURVEY Are you interested in computer science? (y/n): y
#Do you like playing computer games? (y/n): n
#Do you have an Instagram account? (y/n): y
#
#SURVEY RESULTS Interested in computer science: Yes
#Playing computer games: No
#Has an Instagram account: Yes

computer_science = input('SURVEY Are you interested in computer science? (y/n): ')
computer_games = input('Do you like playing computer games? (y/n): ')
Instagram = input('Do you have an Instagram account? (y/n): ')

if computer_science == 'y':
    computer_science = True
    print("SURVEY RESULTS Interested in computer science: Yes")
else:
    computer_science = False
    print("SURVEY RESULTS Interested in computer science: No")

if computer_games == 'y':
    computer_games = True
    print("Playing computer games: Yes")
else:
    computer_games = False
    print("Playing computer games: No")

if Instagram == 'y':
    Instagram = True
    print("Has an Instagram account: Yes")
else:
    Instagram = False
    print("Has an Instagram account: No")

