#Source https://realpython.com/python-rock-paper-scissors/

import random

user_action = input("Enter a choice (rock, paper, scissors): ") #List
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions) #the computer randomly select between the actions
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:  #By comparing the tie condition first, you get rid of quite a few cases.
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
