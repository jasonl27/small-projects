import random

number = random.randint(0,100)
counter = 1
guess = '0'
playAgain = ''

print('\nWelcome to the Number Guessing Game! In this game, you will guess a random number between 0 and 100. Good luck!')
while(int(guess) != number or playAgain.lower() != 'no'):
    guess = input('\nEnter your guess here: ')
    guess = int(guess)

    if(guess>number):
        print('That guess was higher than the number.')
        counter += 1
    elif(guess < number):
        print('That guess was lower than the number.')
        counter += 1
    elif(guess == number):
        print('\nGood job! You guessed the number in {} tries.\n'.format(counter))
        playAgain = input('Would you like to play again? Please enter \'Yes \'or \'No\' ')
        if(playAgain.lower() == 'yes'):
            number = random.randint(0,100)
            counter = 1

print('\nThank you for playing!\n')