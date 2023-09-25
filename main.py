
#base imports do not remove
import random
import os
import time



#variables
guess = True
menuStatus = True
streakScore = 0





#base game function -----------------------------------------------
def game(guess, streakScore):

    os.system("cls")
    print("Guess the number, 0-50")
    number = random.randint(0,50)
    #print(str(number))
    while guess == True:
        playerGuess = int(input(">> Guess: "))
        if playerGuess > number:
            print("Lower")
        if playerGuess < number:
            print("Higher")
        if playerGuess == number:
            os.system("cls")
            print("Correct!")
            
            guess = False
            streakScore = streakScore + 1
            time.sleep(2)
            menu(streakScore)



# MENU SCRIPT -----------------------------------------------------

def menu(streakScore):
    if menuStatus:
        os.system("cls")
        print("Welcome to random number guessing game, please enter a number to continue.")
        print("\n1 - Play game\n2 - Quit\n\nCurrent streak: "+str(streakScore)+"\n\n")
        reply = input(">> ")
        if reply == "1":
            game(guess, streakScore)
        if reply == "2":
            exit()
        if reply != "1" or "2":
            print("Please enter a valid option.")
            time.sleep(1)
            menu(streakScore)
menu(streakScore)        