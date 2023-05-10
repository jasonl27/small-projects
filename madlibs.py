def prompt1():
    name = input('\nChoose a name: ')
    bodyPart = input('Choose a body part: ')
    fluid = input('Choose a type of fluid: ')
    substance = input('Choose a substance: ')
    
    str = '\n' + name + ' is sick with the ' + bodyPart + ' flu. Drink more ' + fluid + ' and take ' + substance + ' as needed.'
    print(str)

def prompt2():
    name = input('\nChoose a name: ')
    noun = input('Choose a noun: ')
    event = input('Choose a event: ')

    str = '\n' + name + ' is too cool for ' + noun + ' class. Instead, he/she will be attending the ' + event
    print(str)

def main():
    play = input("Would you like to play mad libs? If yes, enter \'Y\' ")
    while(play == 'Y'):
        prompt = input('Choose prompt 1 or 2 ')
        if(int(prompt) == 1):
            prompt1()
        elif(int(prompt) == 2):
            prompt2()
        play = input("\nWould you like to play again? Enter 'Y' if Yes. ")

main()