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

game_options = ["rock", "paper", "scissors"]
choices_str = ", ".join(game_options)
winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

#print(choices_str)

for x in range(0, numgames):
    generatednum = random.randint(0,2)
    computerchoice = game_options[generatednum]
    

    #userinput = input("Select rock, paper, or scissors\n")
    userinput = input(f"Enter a choice ({choices_str}): \n")
    print(computerchoice)

    if userinput == computerchoice:
        print(f"You draw {userinput} {computerchoice}")
    elif userinput in winning_moves:
        if winning_moves[userinput] == computerchoice:
            print(f"You won {userinput} {computerchoice}")
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
    os.system("python3 Rockpaperscissors modified.py") # executes a shell command
    