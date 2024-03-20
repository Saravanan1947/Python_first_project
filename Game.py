import random

user_input = input("Enter your choice (stone, paper, scissors): ")
print(user_input)

computer_choice = ["stone", "paper", "scissors"]
system_input = random.choice(computer_choice)
print(system_input)

if user_input.lower() == system_input:
    print("It's a Tie")
elif (user_input.lower() == "stone" and system_input == "scissors") or (user_input.lower() == "paper" and system_input == "stone") or (user_input.lower() == "scissors" and system_input == "paper"):
    print("You are the Winner")
else:
    print("System is the Winner")
