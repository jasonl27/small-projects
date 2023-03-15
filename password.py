import random

print('\nWelcome to the Random Number Generator program! This program will combine uppercase letters, lowercase letters, numbers, and characters to create a random password.')
print('How long would you like your password to be?\n')
pwLen = int(input('Enter a number here: '))

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
char = '!@#$%^&*()'

lowerList = []
for letter in lower:
    lowerList += letter

upperList = []
for letter in upper:
    upperList += letter

numList = []
for number in num:
    numList += number

charList = []
for character in char:
    charList += char

password = ''
while(len(password) < pwLen):
    x = random.randint(1,4)
    if(x == 1):
        y = random.randint(0, len(lowerList)-1)
        password += lowerList[y]
    elif(x == 2):
        y = random.randint(0, len(upperList)-1)
        password += upperList[y]
    elif(x == 3):
        y = random.randint(0, len(numList)-1)
        password += numList[y]
    elif(x == 4):
        y = random.randint(0, len(charList)-1)
        password += charList[y]

print('\nHere is your randomly generated password: ' + password + '\n')