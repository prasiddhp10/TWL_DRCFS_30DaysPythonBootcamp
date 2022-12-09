# Rock Scissor Paper 
import random
user = input("Enter a choice? ")
user_lowercase = user.lower()
print("Your choice is " +user_lowercase)
actions = ["rock", "paper", "scissors"]
choice = random.choice(actions)
if user_lowercase == choice:
    print("Match Draw")
elif user_lowercase == "rock": 
    if choice == "paper":
        print("Oh no! The PC won")
    else: 
        print("Congrats you won the game")
elif user_lowercase == "paper": 
    if choice == "rock":
        print("Congrats you won the game")
    else:
        print("Oh no! The PC won")
else: 
    if choice == "rock":
        print("Oh no! The PC won")
    else: 
        print("Congrats you won the game")
    
print("The PC's choice was : "+choice)