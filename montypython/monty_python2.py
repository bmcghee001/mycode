#!/usr/bin/env python3

round = 0   #  integer round initiated to 0

while(True):    #  sets up an infinite loop condition

    round = round + 1   #  increase the round counter
    print()
    print('Finish the movie title, "Monty Python\'s The Life of ______ "')
    print()
    answer = input()    #  string answer collected from user
#   if (answer == 'Brian'): #  logic to check if user gave correct answer
    if answer.lower() == "brian":
        print()
        print()
        print ('Correct')
        break   #  break statement escapes the while loop
        print()

    elif (round == 3):   #  logic to ensure round has not yet reached 3
        print()
        print('Sorry, the answer was Brian .')
        break   #  break statement escapes the while loop
        print()

    else:   #  if answer was wrong, and round is not yet equal to 3
        print()
        print('Sorry! Try again!')
        print()

