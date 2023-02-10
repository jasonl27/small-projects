import random

print('\nWelcome to Rock Paper Scissors!')

playGame = True
while(playGame == True):
    randomNum = random.randint(1,3)
    if(randomNum == 1):
        compChoice = 'Rock'
    elif(randomNum == 2):
        compChoice = 'Paper'
    elif(randomNum == 3):
        compChoice = 'Scissors'
    
    userChoice = int(input('\nEnter 1 to choose Rock, 2 to choose Paper, and 3 to choose Scissors! '))

    if(randomNum == userChoice):
        print('Computer chose {}. Tie!'.format(compChoice))
    elif(randomNum == 1 and userChoice == 3):
        print('Computer chose {}. You lose!'.format(compChoice))
    elif(randomNum == 3 and userChoice == 1):
        print('Computer chose {}. You win!'.format(compChoice))
    elif(randomNum > userChoice):
        print('Computer chose {}. You lose!'.format(compChoice))
    elif(randomNum < userChoice):
        print('Computer chose {}. You win!'.format(compChoice))
    
    playAgain = input('\nWould you like to play again? Enter \'Y\' or \'N\' ')
    if(playAgain == 'N'):
        playGame = False

print('\nThank you for playing!\n')