
#base imports do not remove
import random
import os
import time



#variables
guess = True
menuStatus = True
streakScore = 0
x = open("high.score", "r")
highScore = x.read()
x.close()





#base game function -----------------------------------------------
def game(guess, streakScore):

    os.system("cls")
    print("Guess the number, 0-50")
    number = random.randint(0,50)
    #print(str(number))
    while guess == True:
        try:
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
                saveGame(streakScore, highScore)
                menu(streakScore, highScore)
                
        #catch error, return back to start. loop try until correct answer.
        except ValueError:
            print("\nPlease enter a number!")
            time.sleep(2)
            os.system("cls")
            game(guess,streakScore)



# MENU SCRIPT -----------------------------------------------------

def menu(streakScore, highScore):
    x = open("high.score" , "r")
    highScore = x.read()
    x.close()
    if menuStatus:
        option = (1,2,3)
        optionName = ["1 - Play Game",
                      "2 - Reset High score",
                      "3 - Quit\n\n"]
        os.system("cls")
        print("Welcome to random number guessing game, please enter a number to continue.\n")
        for i in range(len(optionName)):
            print(optionName[i])
        print("Current streak: "+str(streakScore)+"\n\n"+"Current high score: "+str(highScore))
        reply = input(">> ")
        if reply == "1":
            game(guess, streakScore)
        if reply == "2":
            os.system("cls")
            print("Are you sure you want to clear your high score?\n\n1 - Yes\n2 - No\n\n")
            x = input(">> ")
            if x == "1":
                file = open("high.score", "w")
                file.write(str(0))
                file.close()
                os.system("cls")
                print("High score is now reset.")
                time.sleep(2)
                menu(streakScore, highScore)
            if x == "2":
                menu(streakScore, highScore)
            if x != "1" or "2":
                print("Please enter a valid option.")
                time.sleep(1)
                menu(streakScore, highScore)
            
        if reply == "3":
            os.system("cls")
            print("Thankyou for playing.")
            time.sleep(2)
            exit()
            
        if reply != option:
            print("Please enter a valid option.")
            time.sleep(1)
            menu(streakScore, highScore)
            
# SAVE FILES -----------------------------------------------------

def saveGame(streakScore, highScore):
    x = open("high.score", "r")
    y = x.read(1)
    print(y)
    x.close()
    if int(float(streakScore)) >= int(float(highScore)):
        x = open("high.score", "w")
        x.write(str(streakScore))
        x.close()
    else:
        menu(streakScore, highScore)
        
    
    x.close()
    

#saveGame(streakScore, highScore)
menu(streakScore, highScore)