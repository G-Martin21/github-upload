#From https://github.com/thedanelias/rock-paper-scissors-python/blob/master/rockpaperscissors.py
# modified to make it more streamline, easy to change rules (from classic to Spock) and 
# learn to use f-strings, dictionaries, lists

import random, os, sys 
from os import path

#initial state variables

computerscore = 0
userscore = 0
numgames = int(input("Welcome to rock, paper, scissors.\nHow many games would you like to play?\n"))
userinput = ""
computerchoice = ""
userwin = False
draw = False
choice = ""
clear = lambda: os.system("clear") # the os.system("cls") is old code, 
                #see https://srinimf.com/2018/01/19/three-really-working-commands-to-clear-python-console/

game_options = ["rock", "paper", "scissors", "lizard", "Spock"]
choices_str = ", ".join(game_options)
#numgames = int(input(f"Welcome to ({choices_str}).\nHow many games would you like to play?\n"))

winning_moves = {"rock": ["scissors", "lizard"], "paper": ["rock", "Spock"], "scissors": ["paper", "lizard"],
                 "lizard": ["paper", "Spock"], "Spock": ["scissors", "rock"]}
#winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"} #for the classical games
                 
beats = {("rock", "scissors"): "crushes", ("rock", "lizard"): "crushes",
        ("paper", "rock"): "covers", ("paper", "Spock"): "disaproves"} #personalised messages

for x in range(0, numgames):
    generatednum = random.randint(0,4)
    computerchoice = game_options[generatednum]

    userinput = input(f"Enter a choice ({choices_str}): \n") # using f* strings instead of
                                                #userinput = input("Select rock, paper, or scissors\n")
                                                # so it adapts to changes in options

    if userinput == computerchoice:
        print(f"You draw {userinput} {computerchoice}")
    elif (userinput in winning_moves) and (computerchoice in winning_moves[userinput]): #(winning_moves[userinput] == computerchoice):
        if (userinput, computerchoice) in beats:   #add personalised message
            print(f"You won {userinput} {beats[userinput, computerchoice]} {computerchoice}")
        else:
            print(f"You won {userinput} beats {computerchoice}")
        userscore += 1
    else:
        print(f"You lost {userinput} {computerchoice}")
        computerscore += 1

if userscore > computerscore:
    userwin = True
elif userscore == computerscore:
    draw = True

if userwin == True:
    print("Congratulations, you won!\nYour score:",userscore,"\nComputer's score:",computerscore)
elif draw == True:
    print("You drew!\nYour score:",userscore,"\nComputer's score:",computerscore)
elif userwin == False:
    print("I'm sorry, but you lost.\nYour score:",userscore,"\nComputer's score:",computerscore)

choice = str(input("Would you like to play again? y/n\n"))
if choice == "y":
    clear() # clear the screen2
    source = path.realpath("Rockpaperscissors.py")
    os.system("python3 Rockpaperscissors_modified.py") # executes a shell command
    