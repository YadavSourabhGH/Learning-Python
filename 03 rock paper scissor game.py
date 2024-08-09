import random
import time

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    while True:
        user_choice = input("Enter Your Choice (rock(r), paper(p), scissors(s): ")
        user_choice = user_choice.lower()
        if user_choice not in ["r", "p", "s", "rock", "paper", "scissors"]:
            print("Invalid Choice\n")
        elif user_choice in ["r", "rock"]:
            return "rock"
        elif user_choice in ["p", "paper"]:
            return "paper"
        elif user_choice in ["s", "scissors"]:
            return "scissors"
        else:
            return "Invalid Choice"

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's A Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or          (user_choice == "paper" and computer_choice == "rock") or          (user_choice == "scissors" and computer_choice == "paper"):
        return "You Win"
    else:
        return "Computer Wins"

while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You Choose: ", user_choice)
    print("Computer Choose: ", computer_choice)
    print(determine_winner(user_choice, computer_choice) + "!")
    print("Restarting In 5 Seconds...\n")
    time.sleep(5)