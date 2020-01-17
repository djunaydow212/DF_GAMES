import random
import time

def game_Intro():
    print('DF GAMES PRODUCTIONS....')
    time.sleep(2)
    print('DF GAMES PRESENTS....')
    time.sleep(2)
    print('CAVES OF TIME....')
    print()
    Prologue()

def Prologue():
    print('You have been here before in Snakes Canyon....')
    time.sleep(2)
    print('But last time you did not mention CAVES ....')
    time.sleep(2)
    print('Maybe it is opened after SNOWFALL....')
    time.sleep(2)
    print('Even sunlights going there it is all DARK...')
    time.sleep(2)
    print('Try to find it is sizes you are going FORWARD...')
    time.sleep(2)
    print('..........')
    time.sleep(2)
    print('................')
    time.sleep(2)
    print('........................')
    time.sleep(2)
    print('How much you are Here?....')
    time.sleep(2)
    print('You are hungry....')
    time.sleep(2)
    print('WHAT WILL YOU DO NOW?.....')
    time.sleep(2)
    print('..............')
    print('If you want to go home--->(type "go home")')
    time.sleep(2)
    print('If you want to stay here--->(type "stay here")')
    time.sleep(2)
    print('')

    Prologue = input()
    if Prologue == 'go home':
        go_Home()
    else:
        stay_Here()

def go_Home():
    print()

def stay_Here():
    print()

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    game_Intro()

    print('Do you wanna play again?(type yes or not)')
    playAgain = input()

