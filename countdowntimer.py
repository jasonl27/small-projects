import time

totalTime = input('\nWelcome to the Countdown Timer Program!\n\nHow many seconds would you like the timer to run? Enter in seconds: ')
totalTime = int(totalTime)

while totalTime > 0:
        seconds = int(totalTime % 60)
        minutes = int((totalTime - seconds)/60)
        timer = '\t{:02d}:{:02d}'.format(minutes, seconds)
        print(timer, end="\r")
        time.sleep(1)
        totalTime -= 1